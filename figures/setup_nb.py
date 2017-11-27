# -*- coding: utf-8 -*-
# This sets up basic prerequisites for plotting and simulation notebooks

import sys

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sb

from IPython import get_ipython

from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, pearsonr, linregress
from scipy.io import loadmat

# Path management:

sys.path.append("../lib")

# from analysis.loader import _load
from analysis.helpers import groupexcept, rangemean, rangemean2, preprocess_standard, analysis_lowpass

# IPython-specific setup:

ipython = get_ipython()

ipython.magic("matplotlib inline")
ipython.magic("config InlineBackend.figure_format = 'retina'")
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

# Seaborn/figures:

standard_rc = {
    'lines.linewidth': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'axes.linewidth': .7,

    'axes.labelsize': 6.5,
    'axes.titlesize': 7.5,
    'legend.fontsize': 6,
    'xtick.labelsize': 6.5,
    'ytick.labelsize': 6.5,

    'legend.markerscale': 2,

    'mathtext.default': 'regular',

    'pdf.fonttype': 42,
}

sb.set(style="ticks",
       context="paper",
       rc=standard_rc)

standard_format = (8.3, 11.7)

standard_dpi = 600

# Genotype setup:

gt_colors = {
    'F1 id528 x X154': [0.4] * 3,
    'F1 X154 x GMRSS00324': [0.6] * 3,
    'F1 id528 x GMRSS00324': '#1b9e77',

    'F1 TNT x id548': '#2166ac',
    'OFF': '#2166ac',
    'F1 TNT x id114': '#b2182b',
    'ON': '#b2182b',

    'F1 TNT x X154 (A)': [0.4] * 3,
    'F1 X154 x TNT': [0.4] * 3,
    'F1 TNT x id114 (C)': '#b2182b',
    'F1 TNT x id548 (B)': '#2166ac',
    'F1 id114 x X154 (E)': [0.6] * 3,
    'F1 id548 x X154 (D)': [0.6] * 3,

    'PD': '#35978f',
    'ND': '#bf812d',

    30.0: [0.7]*3,
    60.0: [0.3]*3,
    90.0: [0.1]*3,

    0.0: '#111111',
    1.0: '#999999',
}

gt_alias = {
    'F1 id528 x X154': 'shi control',
    'F1 X154 x GMRSS00324': 'T4/T5 control',
    'F1 id528 x GMRSS00324': 'T4/T5 block',

    'F1 TNT x X154 (A)': 'TNT control',
    'F1 X154 x TNT': 'TNT control',
    'F1 TNT x id114 (C)': 'T5 block',
    'F1 TNT x id548 (B)': 'T4 block',
    'F1 id114 x X154 (E)': 'T5 control',
    'F1 id548 x X154 (D)': 'T4 control',

    u'30.0': u'λ = 30°',
    u'90.0': u'λ = 90°',

    u'PD': 'PD',
    u'ND': 'ND',

    u'0.0': u'Phi (λ = 60°)',
    u'1.0': u'Reverse-phi'
}

# Preprocessing defaults:

standard_tau = 0.1  # s
standard_ci = 95  # %

# Plotting help:

inch2cm = 2.54
cm2inch = 1 / inch2cm


def remove_axis(ax, x=False, y=False):
    if x:
        ax.xaxis.set_visible(False)

    if y:
        ax.yaxis.set_visible(False)

    sb.despine(ax=ax, bottom=x, left=y)


def addaxis(fig, pos, size, letter=None, nudge=0):
    fw, fh = fig.get_size_inches()

    px, py = pos
    sx, sy = size

    ax = fig.add_axes([(px * cm2inch) / fw, (py * cm2inch) / fh, (sx * cm2inch) / fw, (sy * cm2inch) / fh])

    if letter:
        apos = (-0.1 - nudge, 1.12)
        ax.annotate(letter, apos, size=9, xycoords="axes fraction", fontweight="bold")

    return ax


def downsample(signal, factor):
    pad_size = int(np.ceil(len(signal) / float(factor)) * factor - len(signal))
    signal = np.append(signal, [np.nan] * pad_size)

    return sp.nanmean(signal.reshape(-1, factor), axis=1)


def differ(df, which):
    df[which] = df[which].diff() / 0.05
    return df.fillna(method="backfill")


def add_refline(ax, vertical=False, horizontal=False, where=0., xlim=None):
    if xlim is None:
        xlim = ax.get_xlim()

    if horizontal:
        l = ax.plot(xlim, [where, where], linestyle="dotted", zorder=0, color="#444444")
        l[0].set_dashes([1, 1])

    if vertical:
        l = ax.plot([where, where], ax.get_ylim(), linestyle="dotted", zorder=0, color="#444444")
        l[0].set_dashes([1, 1])


def megaplot(x, y, data, ax, color, **kwargs):
    data = data.reset_index()

    lw = mpl.rcParams["lines.linewidth"] * 1.8
    markersize = np.pi * np.square(lw) * 1.0

    a = data.groupby(x)[y].mean().index.values
    b = data.groupby(x)[y].mean().values

    ax.plot(a, b, color=color, linewidth=lw)

    sb.regplot(x, y, x_estimator=np.mean, x_ci=standard_ci, data=data, fit_reg=False, color=color, ax=ax,
               scatter_kws={'s': markersize}, **kwargs)


def draw_reference(ax, corner, size, units, fontsize=10.0, lw=1.0):
    """Draw a reference triangle to indicate scale."""

    cx, cy = corner
    sx, sy = size
    ux, uy = units

    px, py = [cx, cx, cx + sx], [cy + sy, cy, cy]
    ax.plot(px, py, linestyle="-", linewidth=lw, color="black")

    ax.text(cx + 0.5 * sx, cy - 0.6 * sy, u"{0} {1}".format(sx, ux), horizontalalignment='center',
            verticalalignment='center', fontsize=fontsize)
    ax.text(cx - 0.5 * sx, cy + 0.5 * sy, u"{0} {1}".format(sy, uy), horizontalalignment='center',
            verticalalignment='center',
            rotation=90, fontsize=fontsize)
