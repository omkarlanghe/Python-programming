#!/usr/bin/python
#import funtools

print("########Map#########")
def Square(x):
    return x*x

x = map(Square, range(1,30,2))
print(x)
x = map(lambda x: x*x, range(1,30,2))
print(x)

for y in x:
    print(y)

print("#######Filter#########")
def IsEven(x):
    return(x&1) ==0

x = filter(IsEven, range(1, 30))
print(x)

for y in x:
    print(y)

print("########Reduce#########");
def Multiply(x,y):
    return x*y

print reduce(Multiply, range(1,10))

