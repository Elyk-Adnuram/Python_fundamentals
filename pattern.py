'''Program that uses for loop to print a pattern'''
num_of_stars = 5
for i in range(1, 10):
    if i <= num_of_stars:
        print('*' * i)
    else:
        print('*' * (2 * num_of_stars - i))
