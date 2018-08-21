import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from . import _util

def init_defaults():
    sns.set()

def _add_labels(xlabel=None, ylabel=None):
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)

def plot(data, xlabel=None, ylabel=None):
    plt.plot(data)
    _add_labels(xlabel, ylabel)

def swarm(x, y, data, xlabel=None, ylabel=None):
    _ = sns.swarmplot(data=data, x=x, y=y)
    _add_labels(xlabel, ylabel)

def scatter(x, y, data=None, xlabel=None, ylabel=None, **kwargs):
    x, y, = _util.get_x_y(x, y, data)

    _ = plt.plot(x, y, marker='.', linestyle='none', alpha=0.5, **kwargs)
    _add_labels(xlabel, ylabel)

def line(a, b, x = np.array([0, 100]), **kwargs):
    _x = np.array([min(x), max(x)])
    _y = a * _x + b
    _ = plt.plot(_x, _y, **kwargs)

def _ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

def ecdf(data, xlabel=None):
    ecdf_options = {'marker': '.', 'linestyle': 'none'}
    plt.plot(*_ecdf(data), **ecdf_options)
    _add_labels(xlabel, 'ECDF')
    plt.margins(0.02)

def pmf(data, xlabel='', bins=None):
    if bins is None: bins = np.arange(0, max(data) + 2) - 0.5
    
    plt.hist(data, density=True, bins=bins, histtype='step')
    plt.xlabel(xlabel)
    plt.ylabel('p')

def ed_bins(start, end, step):
    return np.arange(start, end+step*2, step=step) - step/2
