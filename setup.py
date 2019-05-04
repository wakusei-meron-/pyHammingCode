#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="PyHammingCode",
      version="0.1",
      author="wakusei-meron-",
      author_email="b0941015@gmail.com",
      description="Simple Code to generate and correct hamming code in python",
      url="https://github.com/wakusei-meron-/pyHammingCode",
      packages=find_packages(),
      entry_points={"console_script": [
          "py_hamming_code = py_hamming_code.py_hamming_code:main"
      ]})
