def RightMostOneBit(no):
    return (no&(no-1))

def main():
    no = eval(input("Enter the number to turn off right most one bit:\n"))
    retVal = RightMostOneBit(no)

    print("number before :", no)
    print("number after :", retVal)

if __name__ == '__main__':
    main()

