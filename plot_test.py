import numpy as np

from . import plot

def test_pmf_bins_can_be_simple_array():
    plot.pmf(data=[0], bins=[0])

def test_pmf_bins_can_be_numpy_array_with_multiple_values():
    plot.pmf(data=[0], bins=np.array([0, 1]))
