#!/usr/bin/python

def Square(x):
    return x*x

x = map(Square, range(1,30,2))
print(x)
x = map(lambda x: x*x, range(1,30,2))
print(x)

for y in x:
    print(y)

def IsEven(x):
    return(x&1) ==0

x = filter(IsEven, range(1, 30))
print(x)

for y in x:
    print(y)
