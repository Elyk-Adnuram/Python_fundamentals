'''Program to make amendments to alternate characters'''

example_string = "Hello World"
output_string = ""
counter = 0 

#Loop through string and create condition to target every 2nd character
for letter in example_string: 
    if counter % 2 == 0:
        output_string += letter.upper()
    else:
        output_string += letter.lower()
    counter += 1
print(output_string)

