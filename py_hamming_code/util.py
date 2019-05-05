from functools import reduce


def parity(bits):
    return reduce(lambda x, y: x ^ y, bits)
