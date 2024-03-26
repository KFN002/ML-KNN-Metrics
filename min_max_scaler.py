import numpy as np


def minmax_scale(X):
    min_vals = X.min(axis=0)
    max_vals = X.max(axis=0)

    range_vals = np.where(min_vals == max_vals, 1, max_vals - min_vals)
    scaled_X = (X - min_vals) / range_vals

    return scaled_X
