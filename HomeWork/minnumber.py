#!usr/bin/python

num1 = eval(input("Enter 1st number:\n"))
num2 = eval(input("Enter 2nd number:\n"))
num3 = eval(input("Enter 3rd number:\n"))

if(num1 < num2 and num1 < num3):
    print(num1 ,"is smallest among three\n")
elif(num2 < num3):
    print(num2 ,"is smallest among three\n")
else:
    print(num3, "is smallest among three\n")

