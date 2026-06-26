"""
The Pointer State Problem (The "Never Pollute Inbound State" Rule)

The Task: Write a while loop logic that takes two user inputs: start and end. Print all the numbers between them.
However, you must adhere strictly to the elite rule: Do not modify the start or end variables directly,
and do not initialize any extra counter variable like i = start.

The 1% Hint: Think about how you can conceptually shift the comparison dynamically inside the loop condition using
standard arithmetic rather than a traditional ascending counter state.
"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
offset = 0

while (start + offset) <= end:
    print(f"{start + offset}, ", end=" ")
    offset += 1

print(f"\n{start}")
print(f"{end}")
