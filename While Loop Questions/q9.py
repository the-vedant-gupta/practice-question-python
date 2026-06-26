"""
Sentinel State Optimization (The Continuous Streams Rule)
The Task: Recreate a dynamic sentinel-controlled loop that processes a continuous stream of integer inputs.
Compute and track two variables concurrently: the maximum value entered and the second maximum value entered.
The loop must exit immediately when 0 is inputted.

The 1% Hint: Do not use any built-in functions or lists to track states.
Initialize your maximum variables using negative infinity as demonstrated in the list analysis section: float('-inf').
"""

# Initialize both maximum tracking states to negative infinity
max1 = float("-inf")
max2 = float("-inf")

print("Enter integers to track the top 2 values (Enter 0 to stop):")

while True:
    num = int(input("Enter a number: "))

    # Check for the sentinel value immediately
    if num == 0:
        break

    # Evaluate incoming state against running maximum boundaries
    if num > max1:
        max2 = max1  # The old maximum cascades down to the second position
        max1 = num  # Update the absolute maximum
    elif num > max2:
        max2 = num  # Update only the second maximum

# Validate if any calculations were made before printing output
if max1 == float("-inf"):
    print("No non-zero numbers were entered.")
elif max2 == float("-inf"):
    print(f"Absolute Maximum: {max1} | Second Maximum: None (Only one number entered)")
else:
    print(f"Absolute Maximum: {max1} | Second Maximum: {max2}")
