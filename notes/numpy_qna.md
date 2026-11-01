# NumPy Basics - QnA Practice

A collection of beginner NumPy practice questions with answers. Try solving each one before looking at the solution!

---

## 1. Creating Arrays

### Q1. Create a 1D array of the numbers 1 to 5
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

### Q2. Create an array of 10 zeros, then an array of 10 ones
```python
zeros = np.zeros(10)
ones = np.ones(10)
print(zeros)
print(ones)
```

### Q3. Create an array of even numbers from 2 to 20 using `arange`
```python
evens = np.arange(2, 21, 2)
print(evens)
```

### Q4. Create an array of 5 numbers evenly spaced between 0 and 1
```python
arr = np.linspace(0, 1, 5)
print(arr)  # [0.   0.25 0.5  0.75 1.  ]
```

### Q5. Create a 3x3 matrix filled with the number 7
```python
mat = np.full((3, 3), 7)
print(mat)
```

---

## 2. Array Attributes

### Q6. Given `arr = np.array([[1, 2, 3], [4, 5, 6]])`, print its shape, number of dimensions, and total number of elements
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3)
print(arr.ndim)   # 2
print(arr.size)   # 6
```

### Q7. Check the data type of an array, and create an integer array as float type explicitly
```python
arr = np.array([1, 2, 3])
print(arr.dtype)  # int32 / int64

float_arr = np.array([1, 2, 3], dtype=float)
print(float_arr.dtype)  # float64
```

---

## 3. Indexing & Slicing

### Q8. From `arr = np.array([10, 20, 30, 40, 50])`, get the first, last, and middle elements
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[2])    # 30
```

### Q9. From the same array, slice out `[20, 30, 40]`
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  # [20 30 40]
```

### Q10. Given a 2D array, extract the element `6` and the last row
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1, 2])   # 6  (row 1, column 2)
print(arr[-1])     # [7 8 9]  (last row)
```

### Q11. Reverse an array using slicing
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[::-1])  # [5 4 3 2 1]
```

---

## 4. Reshaping & Combining

### Q12. Reshape an array of 12 elements into a 3x4 matrix
```python
arr = np.arange(12)
mat = arr.reshape(3, 4)
print(mat)
```

### Q13. Flatten a 2D array back into 1D
```python
mat = np.array([[1, 2], [3, 4]])
flat = mat.flatten()   # or mat.ravel()
print(flat)  # [1 2 3 4]
```

### Q14. Stack two arrays vertically and horizontally
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack([a, b]))  # 2x3, rows stacked
print(np.hstack([a, b]))  # [1 2 3 4 5 6], side by side
```

---

## 5. Math & Broadcasting

### Q15. Add, multiply, and square two arrays element-wise
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print(a ** 2)  # [1 4 9]
```

### Q16. Add 10 to every element of an array (broadcasting)
```python
arr = np.array([1, 2, 3, 4])
print(arr + 10)  # [11 12 13 14]
```

### Q17. Multiply every row of a 2D array by `[1, 10, 100]`
```python
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat * np.array([1, 10, 100]))
# [[  1  20 300]
#  [  4  50 600]]
```

---

## 6. Aggregations

### Q18. Find the sum, mean, min, and max of an array
```python
arr = np.array([3, 7, 1, 9, 4])
print(arr.sum())   # 24
print(arr.mean())  # 4.8
print(arr.min())   # 1
print(arr.max())   # 9
```

### Q19. Find the sum of each row and each column of a 2D array
```python
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat.sum(axis=1))  # [ 6 15] - row sums
print(mat.sum(axis=0))  # [5 7 9] - column sums
```

### Q20. Find the index of the maximum value in an array
```python
arr = np.array([3, 7, 1, 9, 4])
print(arr.argmax())  # 3 (index of value 9)
```

---

## 7. Boolean Indexing & Filtering

### Q21. Get all elements greater than 5 from an array
```python
arr = np.array([3, 7, 1, 9, 4, 12])
print(arr[arr > 5])  # [ 7  9 12]
```

### Q22. Replace all negative values in an array with 0
```python
arr = np.array([-2, 5, -8, 3, -1])
arr[arr < 0] = 0
print(arr)  # [0 5 0 3 0]
```

### Q23. Count how many elements are even
```python
arr = np.array([1, 2, 3, 4, 5, 6])
print((arr % 2 == 0).sum())  # 3
```

---

## 8. Random & NaN

### Q24. Generate 5 random floats between 0 and 1, and 5 random integers between 1 and 10
```python
rng = np.random.default_rng(seed=42)

print(rng.random(5))              # floats in [0, 1)
print(rng.integers(1, 11, 5))     # ints from 1 to 10
```

### Q25. Find the positions of NaN values and replace them with the mean of the non-NaN values
```python
arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])

print(np.isnan(arr))                      # [False  True False  True False]
mean_val = np.nanmean(arr)                # 3.0 (mean ignoring NaNs)
arr[np.isnan(arr)] = mean_val
print(arr)  # [1. 3. 3. 3. 5.]
```

---

## Tips
- Run each snippet yourself and print intermediate results — that's the fastest way to build intuition.
- Remember: NumPy operations are **element-wise** by default, unlike Python lists.
- `axis=0` works down the rows (column results), `axis=1` works across columns (row results).
