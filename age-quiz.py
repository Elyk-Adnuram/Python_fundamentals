'''Program to showcase if, elif and else statements'''

# Obtain user input and set it to an integer
user_age = int(input("Please enter your age \n"))

# if, elif and else statement to check the various conditions
# and print the related user feedback
if user_age > 100:
    print("Sorry, you're dead")
elif user_age >= 65:
    print("Enjoy your retirement")
elif user_age >= 40:
    print("You're over the hill")
elif user_age == 21:
    print("Congrats on your 21st")
elif user_age < 13:
    print("You qualify for the kiddie discount")
else:
    print("Age is but a number")
    