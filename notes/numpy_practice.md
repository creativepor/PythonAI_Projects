# NumPy Practice Questions & Solutions

> **Setup:** Make sure NumPy is installed before running any code.
> ```bash
> pip install numpy
> ```

```python
import numpy as np
```

---

## 🟢 Beginner

---

### Q1. Create a 1D array of numbers from 10 to 50.

```python
arr = np.arange(10, 51)
print(arr)
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
#  31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]
```

---

### Q2. Create a 3x3 matrix filled with zeros, then change the diagonal to 1.

```python
matrix = np.zeros((3, 3))
np.fill_diagonal(matrix, 1)
print(matrix)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Alternative: use np.eye()
identity = np.eye(3)
print(identity)
```

---

### Q3. Create an array of 20 evenly spaced numbers between 0 and 5.

```python
arr = np.linspace(0, 5, 20)
print(arr)
# [0.         0.26315789 0.52631579 0.78947368 1.05263158 1.31578947
#  1.57894737 1.84210526 2.10526316 2.36842105 2.63157895 2.89473684
#  3.15789474 3.42105263 3.68421053 3.94736842 4.21052632 4.47368421
#  4.73684211 5.        ]
```

---

### Q4. Given `[3, 1, 4, 1, 5, 9, 2, 6]`, find mean, median, and standard deviation.

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print("Mean:              ", np.mean(arr))       # 3.875
print("Median:            ", np.median(arr))     # 3.5
print("Standard Deviation:", np.std(arr))        # 2.560...
```

---

### Q5. Reverse a 1D array without using any loop.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = arr[::-1]
print(reversed_arr)
# [8 7 6 5 4 3 2 1]
```

---

### Q6. Create a 4x4 array of random integers between 1 and 100.

```python
arr = np.random.randint(1, 101, size=(4, 4))
print(arr)
# Output will vary, example:
# [[42 17 85  3]
#  [66 91 28 54]
#  [ 7 39 73 11]
#  [62 50 88 23]]
```

---

### Q7. Find all elements greater than 50 in an array.

```python
arr = np.array([10, 55, 23, 78, 45, 90, 12, 67])

# Boolean masking
result = arr[arr > 50]
print(result)
# [55 78 90 67]

# Also get their indices
indices = np.where(arr > 50)
print(indices)
# (array([1, 3, 5, 7]),)
```

---

## 🟡 Intermediate

---

### Q8. Compute the dot product of `a = [1,2,3]` and `b = [4,5,6]` without a loop.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
print(dot_product)
# 32   (1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32)

# Alternative using @ operator
print(a @ b)
# 32
```

---

### Q9. Reshape a 1D array of 12 elements into a 3x4 matrix, then transpose it.

```python
arr = np.arange(1, 13)          # [1, 2, 3, ..., 12]
matrix = arr.reshape(3, 4)
print("Original (3x4):\n", matrix)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

transposed = matrix.T
print("\nTransposed (4x3):\n", transposed)
# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]
```

---

### Q10. Stack two (3x3) arrays vertically and horizontally.

```python
a = np.ones((3, 3))
b = np.zeros((3, 3))

vertical = np.vstack((a, b))    # shape: (6, 3)
print("Vertical Stack:\n", vertical)

horizontal = np.hstack((a, b))  # shape: (3, 6)
print("\nHorizontal Stack:\n", horizontal)
```

---

### Q11. Normalize an array so all values fall between 0 and 1.

```python
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)
# [0.         0.11111111 0.22222222 0.33333333 0.44444444
#  0.55555556 0.66666667 0.77777778 0.88888889 1.        ]
```

---

### Q12. Replace all negative values in an array with 0.

```python
arr = np.array([3, -1, -4, 1, 5, -9, 2, -6])

arr[arr < 0] = 0
print(arr)
# [3 0 0 1 5 0 2 0]

# Non-destructive alternative using np.where
arr = np.array([3, -1, -4, 1, 5, -9, 2, -6])
result = np.where(arr < 0, 0, arr)
print(result)
# [3 0 0 1 5 0 2 0]
```

---

### Q13. Find the index of the max and min value in a 2D array.

```python
arr = np.array([[10, 85, 32],
                [47, 6,  99],
                [73, 21, 54]])

# Index in the flattened array
flat_max_idx = np.argmax(arr)
flat_min_idx = np.argmin(arr)

# Convert to 2D index
max_idx = np.unravel_index(flat_max_idx, arr.shape)
min_idx = np.unravel_index(flat_min_idx, arr.shape)

print("Max value:", arr[max_idx], "at index:", max_idx)  # 99 at (1, 2)
print("Min value:", arr[min_idx], "at index:", min_idx)  # 6  at (1, 1)
```

---

### Q14. Multiply two matrices of shapes (3,2) and (2,4).

```python
a = np.random.randint(1, 10, size=(3, 2))
b = np.random.randint(1, 10, size=(2, 4))

result = np.dot(a, b)           # or: a @ b
print("Shape of a:", a.shape)   # (3, 2)
print("Shape of b:", b.shape)   # (2, 4)
print("Result shape:", result.shape)  # (3, 4)
print(result)
```

---

## 🔴 Advanced

---

### Q15. Extract a sub-matrix from rows 1–3 and columns 2–4 of a 5x5 matrix.

```python
arr = np.random.randint(1, 100, size=(5, 5))
print("Original 5x5 matrix:\n", arr)

# Slicing: rows 1 to 3 (inclusive), columns 2 to 4 (inclusive)
sub_matrix = arr[1:4, 2:5]
print("\nSub-matrix (rows 1-3, cols 2-4):\n", sub_matrix)
```

---

### Q16. Compute the eigenvalues and eigenvectors of a 3x3 matrix.

```python
matrix = np.array([[4, 2, 0],
                   [2, 3, 1],
                   [0, 1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:\n", eigenvalues)
print("\nEigenvectors (columns):\n", eigenvectors)

# Verify: A * v = λ * v  for each eigenpair
for i in range(len(eigenvalues)):
    lhs = matrix @ eigenvectors[:, i]
    rhs = eigenvalues[i] * eigenvectors[:, i]
    print(f"\nEigenvector {i+1} check (should be ~zero):", np.allclose(lhs, rhs))
```

---

### Q17. Generate 1000 random numbers from a normal distribution and verify ~68% fall within 1 std dev.

```python
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)

mean = np.mean(data)
std  = np.std(data)

within_1_std = np.sum(np.abs(data - mean) <= std)
percentage   = (within_1_std / len(data)) * 100

print(f"Mean: {mean:.4f}")
print(f"Std Dev: {std:.4f}")
print(f"Within 1 std dev: {within_1_std}/1000 = {percentage:.1f}%")
# Expected: ~68.2%
```

---

### Q18. Given a 2D array, sort each row independently.

```python
arr = np.array([[3, 1, 4, 1, 5],
                [9, 2, 6, 5, 3],
                [7, 8, 2, 4, 6]])

sorted_arr = np.sort(arr, axis=1)   # axis=1 sorts along columns (each row)
print("Original:\n", arr)
print("\nSorted (each row):\n", sorted_arr)
# [[1 1 3 4 5]
#  [2 3 5 6 9]
#  [2 4 6 7 8]]
```

---

### Q19. Apply z-score normalization to each column of a matrix.

```python
matrix = np.array([[10, 200, 0.5],
                   [20, 150, 1.5],
                   [30, 300, 2.5],
                   [40, 250, 3.5]])

def zscore_normalize(m):
    mean = np.mean(m, axis=0)   # column-wise mean
    std  = np.std(m, axis=0)    # column-wise std
    return (m - mean) / std

normalized = zscore_normalize(matrix)
print("Z-score Normalized:\n", normalized)

# Verify: each column should have mean≈0 and std≈1
print("\nColumn means (should be ~0):", np.mean(normalized, axis=0))
print("Column stds  (should be ~1):", np.std(normalized, axis=0))
```

---

### Q20. Simulate rolling two dice 10,000 times and find the probability of getting a sum of 7.

```python
np.random.seed(0)
n = 10_000

die1 = np.random.randint(1, 7, size=n)   # 1 to 6
die2 = np.random.randint(1, 7, size=n)

sums = die1 + die2
probability = np.sum(sums == 7) / n

print(f"Probability of sum = 7: {probability:.4f}")
# Expected theoretical probability: 6/36 = 0.1667
# Simulated result should be close to 0.1667
```

---

## 🔥 Challenge

---

### Q21. Implement matrix multiplication using only array indexing (no `np.dot` or `@`).

```python
def matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    assert cols_A == rows_B, "Incompatible shapes for matrix multiplication"

    result = np.zeros((rows_A, cols_B))

    for i in range(rows_A):
        for j in range(cols_B):
            # Sum of element-wise products of row i and column j
            result[i, j] = np.sum(A[i, :] * B[:, j])

    return result

A = np.array([[1, 2], [3, 4], [5, 6]])   # (3, 2)
B = np.array([[7, 8, 9], [10, 11, 12]])  # (2, 3)

result = matrix_multiply(A, B)
print("Custom result:\n", result)

# Verify against np.dot
print("np.dot result:\n", np.dot(A, B))
print("Match:", np.allclose(result, np.dot(A, B)))
```

---

### Q22. Create an 8x8 checkerboard pattern (0s and 1s) using only NumPy.

```python
# Method 1: using np.indices
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2]  = 1
checkerboard[::2,  1::2] = 1
print(checkerboard)

# Method 2: elegant one-liner using modulo
checkerboard2 = (np.indices((8, 8)).sum(axis=0)) % 2
print(checkerboard2)

# Output:
# [[0 1 0 1 0 1 0 1]
#  [1 0 1 0 1 0 1 0]
#  [0 1 0 1 0 1 0 1]
#  ...]
```

---

### Q23. Find the top-5 values and their indices without sorting the entire array.

```python
arr = np.random.randint(0, 1000, size=50)
print("Array:", arr)

# np.argpartition is O(n) — much faster than full sort for large arrays
top5_indices = np.argpartition(arr, -5)[-5:]        # indices of top 5
top5_values  = arr[top5_indices]

# Sort the top 5 by value for clean display
sorted_order = np.argsort(top5_values)[::-1]

print("\nTop 5 values:", top5_values[sorted_order])
print("At indices:  ", top5_indices[sorted_order])
```

---

### Q24. Compute the moving average of a 1D array with a window size of 3.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
window = 3

# Method 1: np.convolve
moving_avg = np.convolve(arr, np.ones(window)/window, mode='valid')
print("Moving average:", moving_avg)
# [2. 3. 4. 5. 6. 7. 8. 9.]

# Method 2: manual using cumsum (efficient for large arrays)
def moving_average(a, w):
    cumsum = np.cumsum(a)
    cumsum[w:] = cumsum[w:] - cumsum[:-w]
    return cumsum[w - 1:] / w

print("Moving average (cumsum):", moving_average(arr, window))
```

---

### Q25. Flatten a nested Python list into a NumPy array without any Python loop.

```python
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Method 1: np.array + flatten
arr = np.array(nested).flatten()
print(arr)
# [1 2 3 4 5 6 7 8 9]

# Method 2: np.ravel (returns a view when possible — more memory efficient)
arr2 = np.array(nested).ravel()
print(arr2)
# [1 2 3 4 5 6 7 8 9]

# Method 3: np.concatenate (works even if sublists have different lengths)
arr3 = np.concatenate([np.array(sublist) for sublist in nested])
print(arr3)
# [1 2 3 4 5 6 7 8 9]
```

---

## 📋 Quick Reference

| Function | Purpose |
|---|---|
| `np.array()` | Create array from list |
| `np.zeros(shape)` | Array of zeros |
| `np.ones(shape)` | Array of ones |
| `np.eye(n)` | Identity matrix |
| `np.arange(start, stop)` | Range array |
| `np.linspace(start, stop, n)` | Evenly spaced values |
| `np.random.randint(low, high, size)` | Random integers |
| `np.random.normal(mean, std, size)` | Normal distribution |
| `arr.reshape(shape)` | Reshape array |
| `arr.T` | Transpose |
| `np.dot(a, b)` or `a @ b` | Matrix multiplication |
| `np.vstack / np.hstack` | Stack arrays |
| `np.sort(arr, axis)` | Sort along axis |
| `np.argsort(arr)` | Indices that would sort array |
| `np.argpartition(arr, k)` | Partial sort (top-k, faster) |
| `np.where(condition, x, y)` | Conditional element selection |
| `np.mean / std / median` | Statistics |
| `np.argmax / argmin` | Index of max/min |
| `np.unravel_index(idx, shape)` | Flat index → multi-dim index |
| `np.linalg.eig(matrix)` | Eigenvalues & eigenvectors |
| `np.convolve(a, b)` | Convolution (moving average) |
| `arr.flatten() / arr.ravel()` | Flatten to 1D |
| `np.fill_diagonal(arr, val)` | Set diagonal values |
| `np.allclose(a, b)` | Check if arrays are ~equal |
