"""
Q2. Custom Number Clamping (Expressions & Logic)

Take an integer value, a min_boundary, and a max_boundary as inputs.

Without using any built-in functions like max() or min(), write a conditional block that "clamps" the value.
If it falls below min_boundary, print the min_boundary. If it goes above max_boundary, print the max_boundary.
Otherwise, print the value itself.
"""

min_boundary = int(input("Enter the min: "))
max_boundary = int(input("Enter the max: "))

value = int(input("Enter the value: "))

if value < min_boundary:
    print(f"{min_boundary}")
elif value > max_boundary:
    print(f"{max_boundary}")
else:
    print(f"{value}")
