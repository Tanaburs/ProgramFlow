age = int(input("How old are you? "))

# if age >= 16 and age <= 65:  # complex condition
if 16 <= age <= 65:  # If 16 is less than or equal to age, and age is less than or equal to 65
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

