# Lesson 3: Core Data Structures (Lists, Tuples, Dictionaries, Sets)

# 1. Lists (Ordered, mutable collection)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(2, "mango")
fruits.insert(1, "kiwi")
print("Fruits List:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Fruits List:", fruits.pop())
print("Fruits List:", fruits.remove("mango"))
print("Fruits List:", fruits.clear())
print("Fruits List:", fruits.sort())
print("Fruits List:", fruits.reverse())
print("Fruits List:", fruits.copy())
print("Fruits List:", fruits.index("apple"))
print("Fruits List:", fruits.count("apple"))
print("Fruits List:", fruits.len())

# 2. Tuples (Ordered, immutable collection)
coordinates = (10.0, 20.0)
print("Coordinates Tuple:", coordinates)

# 3. Dictionaries (Key-Value pairs)
student = {
    "name": "Alice",
    "course": "Python Basics",
    "completed_lessons": 3
}, 
{
    "name": "Bob", 
    "course": "Python Advanced", 
    "completed_lessons": 5
}, 
{
    "name": "Charlie", 
    "course": "Python Advanced", 
    "completed_lessons": 7
}
print(f"Students: {student}")

# 4. Sets (Unique elements, unordered)
unique_numbers = {1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10}
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers)
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.add(11))
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.remove(11))
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.discard(11))
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.pop())
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.clear())
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.copy())
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.len())
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.index(11))
print("Unique Numbers Set (duplicates automatically removed):", unique_numbers.count(11))
