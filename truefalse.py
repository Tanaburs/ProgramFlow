# day = "Friday"
# temperature = 30
# raining = False
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

if 0:  # 0 is evaluated to False in a boolean expression
    print("True")  # This condition will never fire as 0 will equate to false
else:
    print("False")

name = input("Please enter your name: ")
# if name:  # Empty strings will evaluate to False in a boolean expression
if name != "":  # This accomplishes the same as above
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")