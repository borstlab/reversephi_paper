import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import numba

measurement_labels = {'stim': 0,
                      'time': 1,
                      'forward': 2,
                      'sideward': 3,
                      'rotation': 4,
                      'x': 5,
                      'y': 6,
                      'path': 7,
                      'temperature': 8,
                      'info1': 9,
                      'info2': 10,
                      'info3': 11}


def strip_nan(a):
    return a[np.logical_not(np.isnan(a))]


@numba.jit()
def lowpass(i, tau, dt):
    o = np.zeros(i.shape)
    alpha = dt / (tau + dt)

    o[0] = i[0]

    for idx in range(1, len(i)):
        o[idx] = alpha * i[idx] + (1 - alpha) * o[idx - 1]

    return o


def analysis_lowpass(df, tau, dt=0.05, axes=['forward', 'rotation']):
    for axis in axes:
        df[axis] = lowpass(df[axis].values, tau, dt)

    return df


def rangemean(df, r, slicealong='time'):
    return np.mean(df.xs(r, level=slicealong))


def rangemean2(df, r, slicealong='time'):
    slice = df.select(lambda x: r[0] < x[slicealong] <= r[1])
    return np.nanmean(slice)


def allexcept(df, *names):
    names = set(names)
    indices = df.index.names

    return [item for item in indices if item not in names]


def groupexcept(df, *names):
    return df.groupby(level=allexcept(df, *names))


def preprocess_standard(data, mean='trial', filter=0.2, subtract=["right", "left"], at="direction"):
    if mean is not None:
        data = groupexcept(data, mean).mean()

    if filter is not None:
        data = groupexcept(data, 'time').apply(analysis_lowpass, tau=filter)

    if subtract is not None:
        data = pd.concat([
                             (data['rotation'].xs(subtract[0], level=at) - data['rotation'].xs(subtract[1],
                                                                                                    level=at)) / 2.,
                             (data['forward'].xs(subtract[0], level=at) + data['forward'].xs(subtract[1],
                                                                                                  level=at)) / 2.],
                         axis=1
        )

    return data


def generate_fly_statistics(flies, path, experiment_name, labels=measurement_labels,
                            dt=0.05, tau_standard=5, openflag=False):
    line_color = 'black'

    def make_hist_plot(axis, data):

        axis.hist(data, bins=100, histtype='step', orientation='horizontal', color=line_color)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        axis.axhline(0, color=line_color, linestyle='--')
        axis.set_frame_on(False)

    def make_plot(axis, data, label, ylims, yaxis=True):

        t = np.linspace(0, n_trials, num=data.shape[0])

        axis.plot(t, data, color=line_color)
        axis.set_xlabel("Trial")
        axis.set_ylabel(label)
        axis.axhline(0, color=line_color, linestyle='--')
        axis.set_ylim(ylims)
        axis.set_xlim([min(t), max(t)])

        axis.get_xaxis().tick_bottom()
        axis.get_yaxis().tick_left()

        if not yaxis:
            axis.get_xaxis().set_visible(False)

        axis.set_frame_on(False)

    for group in flies:
        for fly in flies[group]:

            savename = os.path.join(path, experiment_name, fly[0], 'figures', 'statistics.png')
            print("Generating statistics for {0}".format(fly[0]))

            dims = (3, 3)

            f = plt.figure(figsize=(11.69, 8.27), dpi=100)

            ax_temp = plt.subplot2grid(dims, (2, 0), colspan=2)
            ax_vel = plt.subplot2grid(dims, (0, 0), colspan=2, sharex=ax_temp)
            ax_vel_hist = plt.subplot2grid(dims, (0, 2), sharey=ax_vel)
            ax_rot = plt.subplot2grid(dims, (1, 0), colspan=2, sharex=ax_temp)
            ax_rot_hist = plt.subplot2grid(dims, (1, 2), sharey=ax_rot)

            rawdata = np.load(os.path.join(path, experiment_name, fly[0], 'processeddata', 'data.npy'))

            n_trials = rawdata.shape[0]

            data_vel = lowpass(strip_nan((np.diff(rawdata[:, :, labels['forward'], :], axis=2) / dt).flatten()),
                               tau_standard, dt)
            data_rot = lowpass(strip_nan((np.diff(rawdata[:, :, labels['rotation'], :], axis=2) / dt).flatten()),
                               tau_standard, dt)
            data_temp = strip_nan(rawdata[:, :, labels['temperature'], :].flatten())

            make_hist_plot(ax_rot_hist, data_rot)
            make_hist_plot(ax_vel_hist, data_vel)

            make_plot(ax_vel, data_vel, "Forward speed (cm/s)", [-0.5, 2.0], False)
            make_plot(ax_rot, data_rot, "Turning speed (deg/s)", [-120., 120.], False)
            make_plot(ax_temp, data_temp, "Temperature (deg C)", [20., 40.])

            try:
                setup = BeautifulSoup(open(os.path.join(path, experiment_name, fly[0], 'info.xml')),
                                      "xml").flyinfo.find('setup').string
                genotype = BeautifulSoup(open(os.path.join(path, experiment_name, fly[0], 'info.xml')),
                                         "xml").flyinfo.find('genotype').string
            except:
                setup = "Unknown"
                genotype = "Unknown"

            f.suptitle("{2}: {0} [{1}] on {3}".format(fly[0], genotype, experiment_name, setup))
            f.tight_layout()

            f.savefig(savename)

            if openflag:
                print("Opening...")
                os.system("open {0}".format(savename))