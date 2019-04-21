x = lambda y: y*y
print(x(3))
print(type(x))

x = lambda x,y: x*y
print(x(10,2))
print(type(x))

x = lambda x,y: [x*x, y*y]
print(x(3,4))
print(type(x))

def generator(x):
    return lambda n:n+x

generator_of_5 = generator(5)
print(generator_of_5(10))

generator_of_10 = generator(10)
print(generator_of_10(10))

