def Add(*args):
    print(type(args))
    print(args)

    result = 0

    for x in args:
        result = result + x

    return result

def main():
    print(Add(1,2))
    print(Add(100,20,300,400))

if __name__ == '__main__':
    main()
