#!usr/bin/python

a = int(input("Enter first number:\n"))
b = int(input("Enter second number:\n"))
c = int(input("Enter third number:\n"))

if(a > b and a > c):
    print(a, "is greater\n")
elif(b > c):
    print(b, "is greater\n")
else:
    print(c, "is greater\n")
