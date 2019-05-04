# coding: utf-8
import numpy as np
from py_hamming_code import matrix as mat


class HammingCoder:

    def __init__(self, extended=None):
        """
        init hamming coder
        :param m: check bit size
        """
        self._extended = extended if extended is not None else False

        self._GEN_MAT = mat.GEN_MAT_8_4 if extended else mat.GEN_MAT_7_4
        self._CHECK_MAT = mat.CHECK_MAT_8_4 if extended else mat.CHECK_MAT_7_4
        self._EXTRACT_MAT = mat.EXTRACT_MAT_8_4 if extended else mat.EXTRACT_MAT_7_4
        self._SYNDROME_TO_INDEX_MAT = mat.SYNDROME_TO_INDEX_MAT_8_4 if extended else mat.SYNDROME_TO_INDEX_MAT_7_4

    def calc_parity(self, d):
        return np.dot(self._GEN_MAT, d) % 2

    def correct(self, d):
        _d = np.copy(d)
        s = np.dot(self._CHECK_MAT, _d) % 2
        if self._extended and s[-1] == 0 and np.any(s[:-1]):
            raise Exception("detected double error")
        if np.any(s):
            # modify index start from 0
            i = np.dot(self._SYNDROME_TO_INDEX_MAT, s.T) - 1
            _d[i] = _d[i] ^ 1
        return np.dot(self._EXTRACT_MAT, _d)
