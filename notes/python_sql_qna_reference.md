# Python & SQL QnA Reference

## Python Functions & Defaults

### Q: Which call overrides `currency` to `"USD"` while leaving `tax_rate` at its default?
```python
def build_invoice(customer, items, tax_rate=0.18, currency="INR"):
    ...
```

**A:** Use a keyword argument for `currency`:
```python
build_invoice(some_customer, some_items, currency="USD")
```

---

## Lists and Matrices

### Q: Why does `for row in matrix: print(row)` print entire rows instead of individual numbers?
**A:** Because `matrix` is a list of rows, and each `row` is itself a list. `print(row)` prints the whole list object.

To print individual numbers, use a nested loop:
```python
for row in matrix:
    for num in row:
        print(num)
```

### Q: What does `print(row)` do?
**A:** It prints the entire row list as-is.

### Q: Does `print()` group values automatically?
**A:** No. The `row` variable already holds a list. `print()` just prints that single list object.

---

## SQL Basics

### Q: What does this query output?
```sql
SELECT product_name, COUNT(*) AS n
FROM orders
WHERE status = 'delivered'
GROUP BY product_name
HAVING COUNT(*) > 2;
```
**A:** It returns product names that were delivered more than 2 times, along with their delivery count.

### Q: Capture orders that are "pending" or have no status recorded (NULL).
**A:**
```sql
WHERE status = 'pending' OR status IS NULL
```

### Q: Sum each customer's total spend without under-reporting.
**A:** Initialize the total **outside** the loop:
```python
total = 0
for order in orders:
    total += order.amount
```

---

## Expressions and Operators

### Q: Is `5 + 3` a boolean expression?
**A:** No, it's an arithmetic expression that evaluates to `8` (an integer).

### Q: What does `>=` mean in Python?
**A:** Greater than or equal to.

### Q: Is `>=` the same as strictly greater than?
**A:** No. `>=` includes equality. Strictly greater than is `>`.

---

## String Methods

### Q: What does `.strip()` do?
**A:** Removes leading and trailing whitespace from a string.
```python
"  hello  ".strip()  # "hello"
```

### Q: Does `.strip()` change the original string?
**A:** No. Strings are immutable in Python, so `.strip()` returns a new string.

### Q: What does `.replace()` do? Is it the same as `.strip()`?
**A:** No. `.replace(old, new)` replaces all occurrences of a substring with another substring.
```python
"hello world".replace("world", "Python")  # "hello Python"
```

### Q: Do `.lower()` and `.append()` also return new strings and leave originals unchanged?
**A:**
- `.lower()` returns a new string (strings are immutable).
- `.append()` is a list method that modifies the list in place and returns `None`.

```python
text = "HELLO"
new = text.lower()    # original unchanged

items = [1, 2]
items.append(3)         # modifies items to [1, 2, 3]
```

---

## Python List Filtering

### Q: What does this code do?
```python
scores = [35, 42, 58, 39, 61]
new_scores = []
for score in scores:
    if score > 40:
        new_scores.append(score)
```
**A:** It filters out scores of 40 or below, giving:
```python
new_scores = [42, 58, 61]
```

---

## SQL Ordering and Pagination

### Q: Why does `ORDER BY` need to come before `LIMIT`/`OFFSET`?
**A:** Because without `ORDER BY`, the database returns rows in an unpredictable order. Sorting first makes `LIMIT`/`OFFSET` results consistent and meaningful.

---

## Nested Dictionaries

### Q: How do you get the mouse stock count from this inventory?
```python
inventory = {
    "electronics": {"laptop": 12, "mouse": 45},
    "stationary": {"pen": 200}
}
```
**A:**
```python
inventory["electronics"]["mouse"]  # 45

# Safer version:
inventory.get("electronics", {}).get("mouse")  # 45
```

### Q: Why is `.get()` safer than bracket access?
**A:** Bracket access raises a `KeyError` if the key is missing. `.get()` returns `None` (or a default value) instead of crashing.

---

## SQL Practice Queries

### Q: Flag every transaction larger than the overall average transaction amount.
```sql
SELECT
    b.holder_name,
    t.amount
FROM bank_transactions t
JOIN bank_accounts b
    ON t.account_id = b.account_id
WHERE t.amount > (SELECT AVG(amount) FROM bank_transactions)
ORDER BY t.amount DESC;
```

### Q: Get total scheduled and attended appointments per doctor.
```sql
SELECT
    d.doctor_name,
    COUNT(a.appt_id) AS total_appointments,
    COUNT(a.check_in_time) AS attended
FROM doctors d
JOIN appointments a
    ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name;
```

---

## Python `range()`

### Q: What does `range(20, 20, -1)` produce?
**A:** Empty sequence: `[]` because start equals stop.

### Q: What does `range(20, 10, -1)` produce?
**A:**
```python
20, 19, 18, 17, 16, 15, 14, 13, 12, 11
```

---

## SQL String Case Sensitivity

### Q: If city values are `"PUNE"`, `"Pune"`, and `"pune"`, how many rows does `WHERE city = 'pune'` return?
**A:** Only rows with exactly lowercase `"pune"` (1 row in this case).

To match all case variations:
```sql
WHERE LOWER(city) = 'pune'
```

---

## Python Data Types

### Q: What is the data type of `12`?
**A:** `int` (integer).

### Q: Is `21` (no decimal, no quotes) an `int` in Python?
**A:** Yes.
