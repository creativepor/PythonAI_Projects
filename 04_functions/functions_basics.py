# Lesson 4: Functions & Modular Code

# 1. Defining a basic function
def greet(name="Learner"):
    return f"Hello, {name}! Ready to code today?"

# Calling the function
message = greet("Python Student")
print(message)

# 2. Function with parameters and return value
def calculate_area(width: float, height: float) -> float:
    """Calculates rectangle area given width and height."""
    return width * height

rect_area = calculate_area(5.5, 4.0)
print(f"Rectangle Area (5.5 x 4.0): {rect_area}")
