#WAP to accept a string from user and perform verbing operation.
#!usr/bin/python

s = (input("Enter the string:\n"))

if(len(s) >= 3):
    if(s.endswith('ing')):
        s = s[:-3]+'ly'
    else:
        s = s + 'ing'
print(s)
