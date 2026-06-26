"""
Q3. The Quadratic Classifier (Arithmetic Operators & Conditionals)Given a quadratic equation ax^2 + bx + c = 0,
    take the coefficients a, b, and c as integers from the user.Calculate the discriminant using the formula: D = b^2 - 4ac
    Check the value of D: If D > 0, print "Two Distinct Real Roots".If D == 0, print
    "One Unique Real Root".If D < 0, print "Complex/Imaginary Roots".
"""

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = (b**2) - (4 * a * c)
print(f"Discriminant (D) = {D}")
if D > 0:
    print(f"D = {D}, has Two Distinct Real Roots")
elif D == 0:
    print(f"D = {D}, has One Unique Real Roots")
else:
    print(f"D = {D}, has Complex/Imaginary Roots")
