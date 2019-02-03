def EvenOdd(number):
    if((number&1)==0):
        return True
    else:
        return False

def main():
    num = eval(input("Enter the number to check:\n"))
    retVal = EvenOdd(num);

    if retVal == True:
        print("The number is even\n")
    else:
        print("The number is odd\n")

if __name__ == '__main__':
    main()
