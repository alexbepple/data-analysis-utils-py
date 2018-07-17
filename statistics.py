import numpy as np

default_q = 95

def ci(data, q=default_q):
    diff = 100 - q
    return np.percentile(data, [diff/2, 100-diff/2])

def print_ci(data, q=default_q):
    print('CI({q}%):'.format(q=q), ci(data, q))

def p(condition): return np.sum(condition) / len(condition)
def print_p(condition): print('p =', p(condition))

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0,1]

def diff_of_means(data1, data2): return np.mean(data1) - np.mean(data2)
def print_diff_of_means(data1, data2):
    print('Difference of means:', diff_of_means(data1, data2))

def translate_mean(data, new_mean=0):
    return data - np.mean(data) + new_mean

def lin_fit(x, y): return np.polyfit(x, y, 1)
