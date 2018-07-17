import numpy as np

from . import bootstrap as bs

def test_replicate_returns_numpy_array():
    assert bs.replicate([1], np.mean, size=1) * 2 == np.array([2])
