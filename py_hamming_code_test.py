import numpy as np
import unittest
import numpy.testing as npt
import py_hamming_code as phc

expected = np.zeros(4)


class test_hamming_code_7_4(unittest.TestCase):
    h = phc.HammingCoder(extended=False)

    def test_calc_parity_zero(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 0, 0])), np.array([0, 0, 0, 0, 0, 0, 0]))

    def test_calc_parity_x1(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([1, 0, 0, 0])), np.array([1, 1, 1, 0, 0, 0, 0]))

    def test_calc_parity_x2(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 1, 0, 0])), np.array([1, 0, 0, 1, 1, 0, 0]))

    def test_calc_parity_x3(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 1, 0])), np.array([0, 1, 0, 1, 0, 1, 0]))

    def test_calc_parity_x4(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 0, 1])), np.array([1, 1, 0, 1, 0, 0, 1]))

    def test_x1_error(self):
        d = np.array([1, 0, 0, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x2_error(self):
        d = np.array([0, 1, 0, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x3_error(self):
        d = np.array([0, 0, 1, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x4_error(self):
        d = np.array([0, 0, 0, 1, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p1_error(self):
        d = np.array([0, 0, 0, 0, 1, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p2_error(self):
        d = np.array([0, 0, 0, 0, 0, 1, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p3_error(self):
        d = np.array([0, 0, 0, 0, 0, 0, 1])
        npt.assert_array_equal(self.h.correct(d), expected)


class test_hamming_code_8_4(unittest.TestCase):
    h = phc.HammingCoder(extended=True)

    def test_calc_parity_zero(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 0, 0])), np.array([0, 0, 0, 0, 0, 0, 0, 0]))

    def test_calc_parity_x1(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([1, 0, 0, 0])), np.array([1, 1, 1, 0, 0, 0, 0, 1]))

    def test_calc_parity_x2(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 1, 0, 0])), np.array([1, 0, 0, 1, 1, 0, 0, 1]))

    def test_calc_parity_x3(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 1, 0])), np.array([0, 1, 0, 1, 0, 1, 0, 1]))

    def test_calc_parity_x4(self):
        npt.assert_array_equal(self.h.calc_parity(
            np.array([0, 0, 0, 1])), np.array([1, 1, 0, 1, 0, 0, 1, 0]))

    def test_x1_error(self):
        d = np.array([1, 0, 0, 0, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x2_error(self):
        d = np.array([0, 1, 0, 0, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x3_error(self):
        d = np.array([0, 0, 1, 0, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_x4_error(self):
        d = np.array([0, 0, 0, 1, 0, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p1_error(self):
        d = np.array([0, 0, 0, 0, 1, 0, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p2_error(self):
        d = np.array([0, 0, 0, 0, 0, 1, 0, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p3_error(self):
        d = np.array([0, 0, 0, 0, 0, 0, 1, 0])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_p4_error(self):
        d = np.array([0, 0, 0, 0, 0, 0, 0, 1])
        npt.assert_array_equal(self.h.correct(d), expected)

    def test_double_error(self):
        d = np.array([1, 1, 0, 0, 0, 0, 0, 0])
        with self.assertRaises(Exception) as er:
            self.h.correct(d)
        self.assertEqual(er.exception.args[0], "detected double error")


if __name__ == "__main__":
    unittest.main()
