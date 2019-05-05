# coding: utf-8
import numpy as np
from py_hamming_code import matrix as mat
from py_hamming_code import util


class HammingCoder:

    def __init__(self, m=3, extended=True):
        """
        init hamming coder
        :param m: check bit size
        """
        self._extended = extended
        self._m = m
        self._CHECK_MAT, self._GEN_MAT = mat.gen_matrices(m)
        self._SYNDROME_TO_INDEX_MAT = mat.gen_syndrome_to_index_matrix(m)

    def calc_parity(self, d):
        p = np.dot(d, self._GEN_MAT) % 2
        if self._extended:
            p = np.append(p, util.parity(p))
        return p

    def correct(self, d):
        _d = np.copy(d)
        extended_parity = 0
        if self._extended:
            extended_parity = util.parity(_d)
            _d = _d[:-1]

        s = np.dot(self._CHECK_MAT, _d) % 2

        if self._extended and extended_parity == 0 and np.any(s):
            raise Exception("detected double error")

        s_num = np.dot(s, self._SYNDROME_TO_INDEX_MAT.T).astype(np.int8)

        n = 0
        while s_num > 2 ** n:
            n += 1

        if s_num % (pow(2, n - 1)) == 0:
            _d[-(n + 1)] = _d[-(n + 1)] ^ 1
        else:
            _d[s_num - n - 1] = _d[s_num - n - 1] ^ 1

        return _d[:-self._m]
