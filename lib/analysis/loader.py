import os
import hashlib

import numpy as np
import pandas as pd
from tqdm import tqdm

from .helpers import groupexcept

labels = ['stim_', 'time', 'forward', 'sideward', 'rotation', 'x', 'y', 'path', 'temperature', 'info1', 'info2', 'info3', 'trial']

path_to_cache = os.path.join([os.path.expanduser("~"), ".behaviour/cache.h5"])


def load_force(hash):
    with pd.get_store(path_to_cache) as store:
        return store[hash]


def load(fm, preprocess=True, cached=True):

    if not cached:
        return _load(fm, preprocess)

    else:
        fn = fm.__file__
        p = hashlib.md5(open(fn).read().encode("utf-8")).hexdigest()

        with pd.get_store(path_to_cache) as store:

            if p in store:

                print("Cache hit for hash {0}".format(p))
                return store[p]

            else:

                print("Cache miss for hash {0}".format(p))
                data = _load(fm, preprocess)
                store[p] = data

                return data


def _load(fm, preprocess):

    flies = fm.flies
    path = fm.path
    experiment_name = fm.experiment_name
    mappings = fm.mappings
    dt = fm.dt

    df_l = list()

    for g, fs in flies.items():

        # progress = progressbar.ProgressBar(widgets=['Processing {0} '.format(g), progressbar.Percentage(), progressbar.Bar(), progressbar.ETA()])

        for fly in tqdm(fs):

            fly_name = fly[0]
            fly_trials = fly[2]

            filename = os.path.join(path, experiment_name, fly_name, 'processeddata', 'data.npy')
            data = np.load(filename)[fly_trials, :, :, :]

            data_proc = np.zeros((data.shape[0], data.shape[1], data.shape[2] + 1, data.shape[3]))

            for idx in range(data.shape[0]):
                data_proc[idx, :, 0:12, :] = data[idx, :, :, :]
                data_proc[idx, :, 12, :] = idx

            data_proc = data_proc.transpose((0, 1, 3, 2)).ravel().reshape((-1, 13))

            df = pd.DataFrame(data_proc, columns=labels)

            # translator = lambda x: stim_names[int(x['stim2'])]

            # Stimulus assignment
            base_index = ['genotype', 'flyname']
            stims = np.load(os.path.join(path, experiment_name, fly_name, "stimuli.npy"))

            for category, mapping in mappings.items():

                translator = lambda x: mapping(stims[int(x['stim_']), :])
                df[category] = df.apply(translator, axis=1)
                base_index.append(category)

            base_index.append('trial')
            base_index.append('time')

            df['genotype'] = g
            df['flyname'] = fly_name

            df = df.drop('stim_', 1)
            df.set_index(base_index, inplace=True)

            df_l.append(df)

    full = pd.concat(df_l)

    if preprocess:

        def differ(df):

            df['forward'] = df['forward'].diff() / dt
            df['rotation'] = -1 * df['rotation'].diff() / dt

            return df.fillna(method="backfill")

        full = groupexcept(full, 'time').apply(differ)

    return full
