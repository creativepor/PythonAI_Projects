

import numpy as np

arr = np.array([2, 3, 4, 6, 7])
evens = np.arange(2, 21, 2)
spaced = np.linspace(0, 1, 5)
zeros = np.zeros(10)
ones = np.ones(10)
mat = np.full((3, 3), 7)
print(arr)
print(evens)
print(spaced)
print(zeros)
print(ones)
print(mat)




import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
float_arr = np.array([1, 2, 3], dtype=float)
print(float_arr.dtype)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)




import numpy as np

arr = np.arange(12)
print(arr)
mat = arr.reshape(3, 4)
print(mat)


import numpy as np

mat = np.array([[1, 2], [3, 4]])
flat = mat.flatten()   # or mat.ravel()
print(flat)