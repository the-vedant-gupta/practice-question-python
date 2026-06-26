"""
Q5. The Bitwise-Simulated Multiplier (Ternary & Basic Operators)Take a number as an input.
Write a single-line conditional expression (Ternary Operator) that checks if the number is a multiple of both 4 and 6.

If it is a multiple of both, return its value multiplied by 10.If it isn't, return its value unchanged. Print the final computed value.
"""

n = int(input("Enter the number: "))
# if n % 4 == 0 and n % 6 == 0:
#     value = n * 10
#     print(f"Final value is {value}")
# else:
#     print(f"Final value is {n}")
value = n * 10 if (n % 4 == 0 and n % 6 == 0) else n
print(f"Final value is {value}")
