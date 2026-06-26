"""
Collatz Conjecture Iterator (The Multi-Conditional Engine)
The Task: Implement a while loop that executes the mathematical path known as the Collatz Conjecture for an integer input n.
The structural loop logic must follow these rules at every step:
    If n is even, update it to $n / 2$.
    If n is odd, update it to $3n + 1$.
The system should print the sequence values on a single line and terminate gracefully when n reaches 1.

The 1% Hint: Utilize standard floor division (//) to maintain clean integer outputs instead of standard floats during mutations.
"""

n = int(input("Enter a starting integer for the Collatz sequence: "))

print(f"\nCollatz sequence tracking for state [{n}]:")

# Print the starting state cleanly
print(n, end=" ")

# The loop engine executes until n collapses down to 1
while n > 1:
    print("->", end=" ")

    if n % 2 == 0:
        n = n // 2  # Even rule: State floor division optimization
    else:
        n = 3 * n + 1  # Odd rule: Multiplicative jump step

    print(n, end=" ")

print("\n\n[Sequence Terminated Successfully]")
