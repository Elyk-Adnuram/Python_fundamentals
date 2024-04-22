'''Program that continually asks a user to enter a number'''

user_number = ""
total = 0
count = 0
while user_number != -1:
    user_number = float(input("Please enter a number (-1 to exit): "))
    # condition to break out of the loop
    if user_number == -1:
        break
    # as the user is broken out of the loop the -1 is not added to total or count
    total += user_number
    count +=1
average = (total+1) / (count-1)
print(f"The average is {average}")
