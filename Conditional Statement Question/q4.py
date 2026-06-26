"""
Q4. The Valid Triangle Check (Nested Conditionals)Take three lengths of a triangle's sides (s_1, s_2, s_3)
    as floating-point inputs from the user.

Step 1: Verify if the side lengths can form a valid triangle using the Triangle Inequality Theorem (the sum of any two sides must be strictly
        greater than the third side).
If invalid, print "Invalid Triangle".s_1 + s_2 > s_3  and  s_1 + s_3 > s_2  and s_2 + s_3 > s_1

Step 2: If it is valid, use nested logic to classify it as "Equilateral" (all sides equal), "Isosceles" (two sides equal),
        or "Scalene" (all sides distinct)."""

s_1 = float(input("Enter side1: "))
s_2 = float(input("Enter side2: "))
s_3 = float(input("Enter side3: "))


if s_1 + s_2 > s_3 and s_1 + s_3 > s_2 and s_2 + s_3 > s_1:
    print("It is a Valid Triangle")

    if s_1 == s_2 == s_3:
        triangle = "Equilateral Triangle (all sides equal)"
    elif s_1 == s_2 or s_2 == s_3 or s_1 == s_3:
        triangle = "Isosceles Triangle (Two sides are equal)"
    else:
        triangle = "Scalene Triangle (all sides distinct)"
    print(f"It is a type of {triangle}")
else:
    print("It is an Invalid Triangle")
