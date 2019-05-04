# pyHammingCode
Simple Code to generate and correct hamming code implemented in python

Only support (7,4) hamming code and (8,4) extended hamming code

# Installation

```
pip install git+https://github.com/wakusei-meron-/pyHammingCode.git
```

# Usage

### (7,4) hamming code
```
# init 
>>> from py_hamming_code import py_hamming_code as phc
>>> h = phc.HammingCoder(extended=False)

# calc parity
>>> import numpy as np
>>> h.calc_parity(np.array([0,1,0,1]))
array([0, 1, 0, 0, 1, 0, 1])

# correct
>>> h.correct(np.array([1,1,0,0,1,0,1]))
array([0, 1, 0, 1])
```

### (8,4) extended hamming code
```
# init 
>>> from py_hamming_code import py_hamming_code as phc
>>> h = phc.HammingCoder(extended=True)

# calc parity
>>> import numpy as np
>>> h.calc_parity(np.array([0,1,0,1]))
array([0, 1, 0, 0, 1, 0, 1, 1])

# single error correct
>>> h.correct(np.array([1,1,0,0,1,0,1,1]))
array([0, 1, 0, 1])

# double error detect
>>> h.correct(np.array([1,0,0,0,1,0,1,1]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/a13887/Desktop/PPP/python/audio/PyHammingCode/py_hamming_code/py_hamming_code.py", line 27, in correct
    raise Exception("detected double error")
Exception: detected double error
```
