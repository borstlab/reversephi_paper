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


def highpass(i, tau, dt):
    return i - lowpass(i, tau, dt)


@jit
def fast_discrete_phi(duration, start, stop, lam, jump_width, f_motion, phase_motion, f_flicker, phase_flicker, recfield, delta_phi, dt):
    
    n_t = int(duration / dt)
    n_s = int(recfield / delta_phi)
        
    # Pre-calculate flicker stuff:
    
    motion_counter, flicker_counter = phase_motion, phase_flicker
    curr_color = -1.0
    curr_pos = 0.0
    
    coll_color = np.zeros(n_t)
    coll_pos = np.zeros(n_t)
    
    for tidx in range(n_t):
        
        curr_t = tidx * dt
        
        # Update stuff:
        if start <= curr_t <= stop:
            
            motion_counter += dt * f_motion
            flicker_counter += dt * f_flicker
            
            if flicker_counter > 1.0:
                curr_color *= -1.0
                flicker_counter = 0.0
                
            if motion_counter > 1.0:
                curr_pos -= jump_width
                motion_counter = 0.0
            
        coll_color[tidx] = curr_color
        coll_pos[tidx] = curr_pos
        
    # Build grating:

    d = np.arange(n_s) * delta_phi

    pp, dd = np.meshgrid(coll_pos, d)
    stim = np.sin(2 * np.pi / lam * (pp + dd))

    stim[stim >= 0.0] = 1.0
    stim[stim < 0.0] = 0.0
    
    stim = stim * coll_color
    
    return stim


# Stimuli:

def gaussian_filter(width=0.5, ds=0.1):

    ds = np.arange(-4 * width, 4 * width, ds)
    gauss = lambda x: np.exp(-np.power(x, 2.) / (2 * np.power(width, 2.)))
    g = gauss(ds)
    return g / g.sum()


class DiscretePhi(object):

    def __init__(self, duration=5., cs=(0.1, 0.5), dc=0.3, lam=20., step=4., v=20., flip=0, nd=False):

        self.duration = duration
        self.cs = cs
        self.dc = dc
        self.lam = lam
        self.vel = v
        self.step = step
        self.flip = flip
        self.nd = nd

    def render(self, view, dt, ds=0.1):

        tlam = self.step / self.vel

        n_t = int(np.round(self.duration / dt))

        extent = (view["n_receptors"] + 2) * view["delta_phi"]
        n_s = int(np.round(extent / ds))
        row = np.linspace(0., extent, n_s)

        stim = np.zeros((n_s, n_t))

        curr_c = 1.
        curr_t = 0.
        curr_sh = 0.

        for t in range(stim.shape[1]):

            if curr_t > tlam:

                curr_c = curr_c * -1
                curr_sh += self.step

                curr_t = 0.

            curr_row = np.sin(2 * np.pi / self.lam * (row + curr_sh))
            curr_row[curr_row > 0.] = self.dc

            if self.flip > 1:
                curr_row[curr_row <= 0.] = self.cs[0] if curr_c > 0 else self.cs[1]
            else:
                curr_row[curr_row <= 0.] = self.cs[0]

            stim[:, t] = curr_row
            curr_t += dt

        if not self.nd:
            stim = np.flipud(stim)

        if "filter" in view.keys():
            w = view["filter"]
            f = gaussian_filter(width=w, ds=ds)
            stim = np.apply_along_axis(arr=stim, axis=1, func1d=lambda a: np.convolve(a, f, mode="same"))

        dets = np.linspace(np.round(view["delta_phi"] / ds), (extent - 2 * view["delta_phi"]) / ds, view["n_receptors"], endpoint=True)
        return stim[dets.astype(np.int), :], stim


class FastDiscretePhi(object):
    def __init__(self, lam, vel, duration, start, stop, flip, nd):
        self.lam = lam
        self.vel = vel
        self.duration = duration
        self.start = start
        self.stop = stop
        self.flip = flip
        self.nd = nd

    def render(self, recfield, delta_phi, true_dt):

        n_rec = int(recfield / delta_phi)
        dt = delta_phi / self.vel

        t = np.arange(0.0, self.duration, dt)

        p = np.zeros(len(t))
        start_, stop_ = int(self.start / dt), int(self.stop / dt)
        p[start_:stop_] = -1 * self.vel

        d = np.arange(n_rec) * delta_phi + 20

        pp, dd = np.meshgrid(dt * p.cumsum(), d)
        stim = np.sin(2 * np.pi / self.lam * (pp + dd))

        stim[stim >= 0.0] = 1.0
        stim[stim < 0.0] = 0.0

        if self.flip:
            flipvec = np.ones(len(t))
            flipvec[start_:stop_:2] = -1.0
            stim = stim * flipvec

        if self.nd:
            stim = np.flipud(stim)

        repfac = int(dt / true_dt)
        assert repfac > 1
        return stim.repeat(repfac, axis=1)


class FastDecoupledPhi(object):
    def __init__(self, duration, start, stop, lam, jump_width, f_motion, phase_motion, f_flicker, phase_flicker):
        self.duration = duration
        self.start = start
        self.stop = stop
        self.lam = lam
        self.jump_width = jump_width
        self.f_motion = f_motion
        self.phase_motion = phase_motion
        self.f_flicker = phase_flicker
        self.phase_flicker = phase_flicker
        
    def render(self, recfield, delta_phi, dt):
        return fast_discrete_phi(duration=self.duration, start=self.start, stop=self.stop, lam=self.lam,
                                    jump_width=self.jump_width, f_motion=self.f_motion, phase_motion=self.phase_motion,
                                    f_flicker=self.f_flicker, phase_flicker=self.phase_flicker, recfield=recfield, delta_phi=delta_phi, dt=dt)


class FastSine(object):
    def __init__(self, lam, vel, duration, start, stop, nd, phaseshift):
        self.lam = lam
        self.vel = vel
        self.duration = duration
        self.start = start
        self.stop = stop
        self.nd = nd
        self.phaseshift = phaseshift

    def render(self, recfield, delta_phi, dt):

        n_rec = int(recfield / delta_phi)
        t = np.arange(0.0, self.duration, dt)

        p = np.zeros(len(t))
        start_, stop_ = int(self.start / dt), int(self.stop / dt)
        p[start_:stop_] = -1 * self.vel

        d = np.arange(n_rec) * delta_phi + self.phaseshift

        pp, dd = np.meshgrid(dt * p.cumsum(), d)
        stim = np.sin(2 * np.pi / self.lam * (pp + dd))

        if self.nd:
            stim = np.flipud(stim)

        return stim