# Lesson 2: Control Flow (Conditionals & Loops)

# 1. Conditionals (if, elif, else)
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Need Improvement")

# 2. For Loop (Iterating over a range)
print("\n--- For Loop Example ---")
for i in range(1, 6):
    print(f"Count: {i}")

# 3. While Loop
print("\n--- While Loop Example ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1
print("Blast off! 🚀")
