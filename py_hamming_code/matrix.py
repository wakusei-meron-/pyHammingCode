import numpy as np


def gen_matrices(m):
    """
    :param m: check bit size
    :return: parity_check_matrix, generator_matrix
    """
    if m < 2:
        raise Exception("invalid check bit size")

    n = 2 ** m - 1
    k = n - m
    column_values = np.array([[x] for x in range(2 ** m) if (x & (x - 1))])
    a = np.zeros((k, m), dtype=np.int8)
    for i, row in enumerate(column_values):
        a[i] = np.array(list(bin(row[0])[2:].zfill(m))).astype(np.int8)
    h = np.concatenate((a.T, np.eye(m, dtype=np.int8)), axis=1)
    g = np.concatenate((np.eye(k, dtype=np.int8), a), axis=1)
    return h, g


def gen_syndrome_to_index_matrix(m):
    return np.ones(m) * 2 ** np.arange(m)[::-1]
