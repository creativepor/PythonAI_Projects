# Lesson 5: Modules and File Operations

import math
import datetime

# 1. Using Python Built-in Standard Library Modules
print(f"Current Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Square root of 16 using 'math' module: {math.sqrt(16)}")

# 2. Writing to a text file
sample_text_path = "sample_output.txt"
with open(sample_text_path, "w", encoding="utf-8") as f:
    f.write("Python Learning Journal\n")
    f.write("Line 1: Understood variables\n")
    f.write("Line 2: Practiced loops and functions\n")

print(f"\nSuccessfully wrote data to '{sample_text_path}'")

# 3. Reading from a text file
with open(sample_text_path, "r", encoding="utf-8") as f:
    content = f.read()

print("\n--- File Content Read Back ---")
print(content)
