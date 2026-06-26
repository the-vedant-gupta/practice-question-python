# """
# Efficient Factorization Limit (The Optimized Search Bound)During the "Print All Factors"
# The Task: Write an optimized while loop that counts and prints all unique factors of a given number,
# but the loop control condition must not run beyond the square root of the number ($\sqrt{num}$).

# The 1% Hint: Every time you find a factor i such that num % i == 0, you automatically uncover its paired factor counterpart via num // i.
# Build your while condition using i * i <= num to keep the computational complexity low.
# """

num = int(input("Enter a number to find its factors: "))
i = 1

print(f"\nThe unique factor pairs of {num} are:")

while i * i <= num:
    if num % i == 0:
        paired_factor = num // i

        if paired_factor != i:
            # Print the pair separated by an arrow, and end with a structural pipe
            print(f"[{i} -> {paired_factor}]", end="  |  ")
        else:
            # Handle perfect square middle boundary cleanly
            print(f"[{i} (Perfect Square Root)]", end="")

    i += 1

print()  # Clean exit newline
