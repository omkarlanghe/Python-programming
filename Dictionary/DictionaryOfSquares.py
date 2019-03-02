def DictionaryOfSquares(number):
    result = {}
    for x in range(1,number+1):
        result[x] = x * x

    return result

def main():
    number = eval(input("Enter number:\n"))
    retVal = DictionaryOfSquares(number)

    print(retVal)

if __name__ == '__main__':
    main()

