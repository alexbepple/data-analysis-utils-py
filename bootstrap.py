import numpy as np

from . import statistics as stat

default_size = 10**4

def unzip2(iterable):
    rx, ry = zip(*iterable)
    return list(rx), list(ry)

def resample(data): return np.random.choice(data, len(data))
def resample_pairs(x, y):
    # in case we have sth with weird index here, e.g. Series
    _x = np.array(x)
    _y = np.array(y)

    indices = np.arange(0, len(_x))
    return unzip2([(_x[i], _y[i]) for i in resample(indices)])

def replicate(data, calc_statistic, size=default_size):
    return np.array([calc_statistic(resample(data)) for _ in range(size)])

def replicate2(data1, data2, calc_statistic, size=default_size):
    return np.array([calc_statistic(resample(data1), resample(data2)) for _ in range(size)])

def replicate_pairs(x, y, f, size=default_size):
    return np.array([f(*resample_pairs(x, y)) for _ in range(size)])

def lin_fit(x, y, size=default_size):
    return unzip2([stat.lin_fit(*resample_pairs(x, y)) for _ in range(size)])
