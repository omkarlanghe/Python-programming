first_string = input("Enter 1st string:\n")
sec_string = input("Enter 2nd string:\n")

firstPart = first_string[:2]
secPart = sec_string[:2]

first_string = secPart + first_string[2:]
sec_string = firstPart + sec_string[2:]

print(first_string)
print(sec_string)
