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

from analysis.loader import _load
from analysis.helpers import groupexcept, rangemean, rangemean2, preprocess_standard, analysis_lowpass

# IPython-specific setup:

ipython = get_ipython()

ipython.magic("matplotlib inline")
ipython.magic("config InlineBackend.figure_format = 'retina'")
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")