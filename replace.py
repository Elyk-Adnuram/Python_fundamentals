'''Program to showcase the replace and upper functions'''

# Declare string variable
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Reprint sentence removing exclamation marks using replace function
no_exclamation_sentence = sentence.replace("!", " ")
print(no_exclamation_sentence)

# Reprint sentence in uppercase
uppercase_sentence = no_exclamation_sentence.upper()
print(uppercase_sentence)

# Reprint sentence in reverse
reversed_sentence = no_exclamation_sentence[::-1]
print(reversed_sentence)
