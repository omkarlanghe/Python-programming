#WAP to accept string from user and return a string having 1st two and last two characters of input string
#!usr/bin/python

input_string = input("Enter the string:\n")
first_two = input_string[0:2]

length = len(input_string);

last_two = input_string[length-2:]
print("First two characters from input string are: ", first_two)
print("Last two characters from input string are:", last_two)

print("string with fist and last two characters is: ",first_two + last_two)
