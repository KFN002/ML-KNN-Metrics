import numpy as np


def onehot_encoding(x):
    objects = len(x)
    categories, indices = np.unique(x, return_inverse=True)
    num_values = len(categories)

    encoding_matrix = np.zeros((objects, num_values), dtype=int)

    for i, index in enumerate(indices):
        encoding_matrix[i, index] = 1

    return encoding_matrix
