"""
Digital Root Extraction (The State Compaction Loop)
The Task: Write a program that takes a massive integer input (e.g., 9876) and uses nested while loops
to continually sum its digits until a single-digit answer is produced.

For example: 9 + 8 + 7 + 6 = 30 --> 3 + 0 = 3. Your output should be 3.

The 1% Hint: The outer loop monitors the ultimate state of the cumulative sum,
while the inner loop breaks down the current number using num % 10 and num // 10
"""

base_num = int(input("Enter the number: "))
num = base_num

while num > 9:
    digit_sum = 0

    while num > 0:
        last_digit = num % 10
        digit_sum += last_digit
        num = num // 10
    num = digit_sum

print(f"The digital root of {base_num} is: {num}")
