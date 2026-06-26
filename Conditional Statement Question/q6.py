"""
Q6. Automated Billing with Stacked Slabs (Complex Else-If)An energy company charges consumption using tiered pricing slabs:
    First 100 units --> ₹4.00 / unit
    Next 200 units (101 to 300) --> ₹6.50 / unit
    Units above 300 --> ₹9.00 /unit
Take the total units used as an integer input.

Write a precise logic chain to calculate the final bill amount. (e.g., If the user consumes 350 units,
the cost is calculated as (100 x 4) + (200 x 6.5) + (50 x 9).
"""

units = int(input("Enter the total units consumed: "))
bill_amount = 0.0

# Tier 1: 100 units or below
if units <= 100:
    bill_amount = units * 4.00

# Tier 2: Above 100 but up to 300 units
elif units <= 300:
    # 100 units at ₹4.00 + remaining units at ₹6.50
    bill_amount = (100 * 4.00) + ((units - 100) * 6.50)

# Tier 3: Everything above 300 units
else:
    # 100 units at ₹4.00 + 200 units at ₹6.50 + leftover units at ₹9.00
    bill_amount = (100 * 4.00) + (200 * 6.50) + ((units - 300) * 9.00)

print(f"Total Electricity Bill: ₹{bill_amount:.2f}")
