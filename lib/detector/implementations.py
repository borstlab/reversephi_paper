import numpy as np
from numba import jit


# Filters:

@jit
def lowpass(i, tau, dt):
    out = np.zeros_like(i)
    out[:, 0] = i[:, 0]

    alpha = dt / (dt + tau)

    for l in range(i.shape[0]):
        for t in range(1, i.shape[1]):
            out[l, t] = alpha * i[l, t] + (1 - alpha) * out[l, t - 1]

    return out


@jit
def highpass(i, tau, dt):
    return i - lowpass(i, tau, dt)


# Detectors:


class FourQ(object):
    def __init__(self,
                 tau_hp=0.25,
                 tau_lp=0.05,
                 dc=0.0,
                 nd_weight=1.0,
                 dt=0.001):
        self.dt = dt
        self.tau_hp = tau_hp
        self.tau_lp = tau_lp
        self.dc = dc
        self.nd_weight = nd_weight

    def detect(self, s):
        s_ = highpass(s, self.tau_hp, self.dt) + self.dc * s
        sf = lowpass(s_, self.tau_lp, self.dt)

        o = sf[0:-1, :] * s_[1:, :] - self.nd_weight * sf[1:, :] * s_[0:-1, :]

        return o


class FourQDelay(object):
    def __init__(self,
                 tau_hp=0.25,
                 tau_lp=0.05,
                 delay=0.01,
                 dc=0.0,
                 nd_weight=1.0,
                 dt=0.001):
        self.dt = dt
        self.tau_hp = tau_hp
        self.tau_lp = tau_lp
        self.delay = delay
        self.dc = dc
        self.nd_weight = nd_weight

        assert self.delay > 0.0

    def detect(self, s):
        s_ = highpass(s, self.tau_hp, self.dt) + self.dc * s

        # This introduces a TRUE DELAY, similar to Tuthill et al. (2011)
        s_delayed = np.zeros_like(s_)
        delay_ = np.ceil(self.delay / self.dt).astype(np.int)
        s_delayed[:, delay_:] = s_[:, :s_.shape[1]-delay_]

        sf = lowpass(s_delayed, self.tau_lp, self.dt)

        o = sf[0:-1, :] * s_[1:, :] - self.nd_weight * sf[1:, :] * s_[0:-1, :]

        return o


class TwoQ(object):
    def __init__(self,
                 tau_hp=(0.25, 0.25),
                 tau_lp=(0.05, 0.05),
                 dc=(0., 0.),
                 nd_weights=(1., 1.),
                 pathway_weights=(1., 1.),
                 offsets=(0., 0.),
                 dt=0.001):
        self.dt = dt
        self.tau_hp = tau_hp
        self.tau_lp = tau_lp
        self.dc = dc
        self.nd_weights = nd_weights
        self.pathway_weights = pathway_weights
        self.offsets = offsets

    def detect(self, s):
        i_on, i_off = highpass(s, self.tau_hp[0], self.dt) + self.dc[0] * s, \
                      highpass(s, self.tau_hp[1], self.dt) + self.dc[1] * s

        s_on, s_off = np.maximum(i_on - self.offsets[0], 0.), \
                      -1 * np.minimum(i_off - self.offsets[1], 0.)

        w_on, w_off = self.nd_weights[0], self.nd_weights[1]

        sf_on = lowpass(s_on, self.tau_lp[0], self.dt)
        sf_off = lowpass(s_off, self.tau_lp[1], self.dt)

        o_on1 = sf_on[0:-1, :] * s_on[1:, :]
        o_on2 = s_on[0:-1, :] * sf_on[1:, :]
        o_on = o_on1 - w_on * o_on2

        o_off1 = sf_off[0:-1, :] * s_off[1:, :]
        o_off2 = s_off[0:-1, :] * sf_off[1:, :]
        o_off = o_off1 - w_off * o_off2

        o = self.pathway_weights[0] * o_on + self.pathway_weights[1] * o_off

        return o


class HRBL(object):
    def __init__(self,
                 tau_hp=(0.25, 0.25),
                 tau_lp=(0.05, 0.05),
                 dc=(0., 0.),
                 nd_weights=(1., 1.),
                 pathway_weights=(1., 1.),
                 offsets=(0., 0.),
                 hrbl_offset=0.1,
                 dt=0.001):
        self.dt = dt
        self.tau_hp = tau_hp
        self.tau_lp = tau_lp
        self.dc = dc
        self.nd_weights = nd_weights
        self.pathway_weights = pathway_weights
        self.offsets = offsets
        self.hrbl_offset = hrbl_offset

    def detect(self, s):
        i_on, i_off = highpass(s, self.tau_hp[0], self.dt) + self.dc[0] * s, \
                      highpass(s, self.tau_hp[1], self.dt) + self.dc[1] * s

        s_on, s_off = np.maximum(i_on - self.offsets[0], 0.), \
                      -1 * np.minimum(i_off - self.offsets[1], 0.)

        w_on, w_off = self.nd_weights[0], self.nd_weights[1]

        sf_on = lowpass(s_on, self.tau_lp[0], self.dt)
        sf_off = lowpass(s_off, self.tau_lp[1], self.dt)

        o_on1 = sf_on[0:-2, :] * s_on[1:-1, :] / (self.hrbl_offset + sf_on[2:, :])
        o_on2 = s_on[0:-2, :] * sf_on[1:-1, :] / (self.hrbl_offset + s_on[2:, :])
        o_on = o_on1 - w_on * o_on2

        o_off1 = sf_off[0:-2, :] * s_off[1:-1, :] / (self.hrbl_offset + sf_off[2:, :])
        o_off2 = s_off[0:-2, :] * sf_off[1:-1, :] / (self.hrbl_offset + s_off[2:, :])
        o_off = o_off1 - w_off * o_off2

        o = self.pathway_weights[0] * o_on + self.pathway_weights[1] * o_off

        return o
