# Python Basics - QnA Practice

A collection of very basic Python coding questions with answers for beginners.

---

## 1. Variables & Output

### Q1. Print "Hello, World!"
```python
print("Hello, World!")
```

### Q2. Create two variables `a` and `b`, assign them numbers, and print their sum
```python
a = 5
b = 3
print(a + b)
```

### Q3. Ask the user for their name and print a greeting
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

## 2. Conditionals

### Q4. Check if a number is positive, negative, or zero
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### Q5. Determine if a year is a leap year
```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

### Q6. Find the largest of three numbers
```python
a, b, c = 10, 25, 15
print(max(a, b, c))
```

---

## 3. Loops

### Q7. Print numbers from 1 to 10 using a `for` loop
```python
for i in range(1, 11):
    print(i)
```

### Q8. Print the multiplication table of a given number
```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)
```

### Q9. Calculate the sum of all numbers from 1 to 100
```python
print(sum(range(1, 101)))
```

### Q10. Print numbers from 0 to 9
```python
for i in range(10):
    print(i)
```

### Q11. Print even numbers from 2 to 20
```python
for i in range(2, 21, 2):
    print(i)
```

### Q12. Print numbers from 10 down to 1 (countdown)
```python
for i in range(10, 0, -1):
    print(i)
```

### Q13. Print the first 5 multiples of 7
```python
for i in range(1, 6):
    print(7 * i)
```

### Q14. Ask the user for `n`, then print numbers from 1 to `n`
```python
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)
```

### Q15. Find the sum of even numbers from 1 to 50
```python
total = 0
for i in range(2, 51, 2):
    total += i
print(total)
```

### Q16. Count how many numbers from 1 to 100 are divisible by 3
```python
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)
```

### Q17. Print the sum of squares from 1² to 5²
```python
total = 0
for i in range(1, 6):
    total += i ** 2
print(total)  # 55
```

### Q18. Print a row of 5 stars: `*****`
```python
for i in range(5):
    print("*", end="")
print()
```

### Q19. Print a triangle (1 star, then 2, then 3, up to 5)
```python
for i in range(1, 6):
    print("*" * i)
```

### Q20. Print this pattern using `range()`:
```
1
12
123
1234
12345
```
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### Q21. Print every second character of a string using index + `range()`
```python
s = "Python"
for i in range(0, len(s), 2):
    print(s[i], end="")
print()
```

### Q22. Double each number in a list using `range(len())`
```python
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)
```

### Q23. Check if a number is prime using `range()`
```python
n = int(input("Enter a number: "))
is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not prime")
```

### Q24. Print the Fibonacci series up to `n` terms
```python
n = int(input("How many terms? "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

**Quick reference — `range()` forms:**

| Form | Example | Output |
|------|---------|--------|
| `range(stop)` | `range(5)` | 0, 1, 2, 3, 4 |
| `range(start, stop)` | `range(2, 6)` | 2, 3, 4, 5 |
| `range(start, stop, step)` | `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| Negative step | `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

---

## 4. Strings & Lists

### Q25. Reverse a string
```python
s = input("Enter a string: ")
print(s[::-1])
```

### Q26. Count how many vowels are in a string
```python
s = input("Enter a string: ")
count = sum(1 for ch in s if ch.lower() in "aeiou")
print(count)
```

### Q27. Find the largest number in a list
```python
numbers = [4, 7, 1, 9, 3]
print(max(numbers))
```

---

## 5. Functions

### Q28. Write a function that returns the square of a number
```python
def square(n):
    return n * n

print(square(4))
```

### Q29. Write a function that checks if a string is a palindrome
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))
```

### Q30. Write a function that returns the factorial of a number
```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
```
