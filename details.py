'''
Ask the user for their name, age, house number and street name 
and create variables for each value
Print out a sentence using all the variables
'''
# use input function to obtain data from user
user_name = input("Please provide your name: ")
user_age = input("Please provide your age: ")
house_number = input("Please provide your house number: ")
street_name = input("Please provide your street name: ")
# Multi-line string used in print statement
print(f"""This is {user_name}. He is {user_age}
years old and lives at house number {house_number} on {street_name} Street""")
