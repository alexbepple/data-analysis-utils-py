import numpy as np

from . import plot
from . import bootstrap as bs
from . import statistics as stat
from . import _util

def plot_lin_fit(x=None, y=None, data=None, xlabel=None, ylabel=None, **kwargs):
    x_data, y_data = _util.get_x_y(x, y, data)

    plot.line(*stat.lin_fit(x_data, y_data), x=x_data, **kwargs)
    plot.scatter(x, y, data=data, xlabel=xlabel, ylabel=ylabel, **kwargs)

def est_lin_fit(x, y, data=None, **_):
    x, y = _util.get_x_y(x, y, data)

    a, b = stat.lin_fit(x, y)
    a_reps, b_reps = bs.lin_fit(x, y)

    print('a =', a)
    stat.print_ci(a_reps)
    print('b =', b)
    stat.print_ci(b_reps)

def est_statistic(x, func, label='Value', q=stat.default_q):
    print(label + ':', func(x))
    stat.print_ci(bs.replicate(x, func), q=q)

def est_statistic_pairs(x=None, y=None, data=None, f=None, label='Value', q=stat.default_q, **kwargs):
    x_data, y_data = _util.get_x_y(x, y, data)
    
    print(label + ':', f(x_data, y_data))
    stat.print_ci(bs.replicate_pairs(x_data, y_data, f=f), q=q)
