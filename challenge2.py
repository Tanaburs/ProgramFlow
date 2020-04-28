#  Write a small program to ask for a name and an age.

#  When both values have been entered, check if the person is the right age to go on an 18-30
#  holiday (they must be over 18 and under 31).

#  If they are, welcome them to the holiday, otherwise print a (polite) message refusing them
# entry.

#  Our programs expect valid input.  We'll see how to handle invalid numbers, later in the
#  course.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if name:
    if 18 <= age <= 30:
        print("Welcome to the holiday {}!".format(name))
    else:
        print("You are not eligible")
else:
    print("Are you the man with no name?")
