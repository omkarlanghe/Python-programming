def variableArgsDictionary(a, b, *args, **kwargs):
    print(a, b)
    print(type(args), type(kwargs))

    for x in args:
        print(x)

    for x in kwargs:
        print(x, kwargs[x])

def main():
    variableArgsDictionary(10,20,1,2,3,4,5,6,7, name = "omkarlanghe", hobby = "programming")

if __name__ == '__main__':
    main()

