"Program to showcase Logical Programming - Operators"

# Obtain user input for swimming, cycling and running time
swimming_time = int(input("Please enter your swimming time in minutes: "))
cycling_time = int(input("Please enter your swimming time in minutes: "))
running_time = int(input("Please enter your swimming time in minutes: "))

# Sum user inputs and display the total time
total_time = swimming_time + cycling_time + running_time

# Create conditional statements to determine award user will receive based on time
if total_time <= 100:
    print(f"Total time is {total_time} and your award is Provincial Colours")
elif total_time >= 101 and total_time <= 105:
    print(f"Total time is {total_time} and your award is Provincial Half Colours")
elif total_time >= 106 and total_time <= 110:
    print(f"Total time is {total_time} and your award is Provincial Scroll")
else:
    print(f"Total time is {total_time} and there is no reward")
