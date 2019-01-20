#!/usr/bin/python

s = input("Enter the string:")
result = s[0]+s[1:].replace(s[0],"*")
print("replaced string is: "+ result);
