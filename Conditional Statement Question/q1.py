"""
Q1. The Advanced Bouncer (Logical Operators & Inputs)

Create a script that takes three inputs: a person's age, whether they have a VIP Pass (True/False), and whether they are blacklisted (True/False).

Rules: A person can enter only if they are 18 or older AND have a valid VIP Pass.
However, regardless of age or VIP status, if they are blacklisted, access is strictly denied.
Print "Access Granted" or "Access Denied".
"""

person_age = int(input("Enter the age = "))
is_blacklisted = input("You are balcklisted? (True or False): ") == "True"
has_VIP = input("You have a VIP pass? (True or False): ") == "True"

# if person_age >= 18 and has_VIP and not is_blacklisted:
#     print("Access Granted")
# else:
#     print("Access Denied")

if is_blacklisted:
    print("Access Denied (Blacklisted)")
else:
    if person_age >= 18 and has_VIP:
        print("Access Granted")
    else:
        print("Access Denied")
