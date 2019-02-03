def DivisibleBy_8(number):
    if((number&7) == 0):
        return True
    else:
        return False

def main():
    number = eval(input("Enter the number to check:\n"))

    retVal = DivisibleBy_8(number)

    if retVal == True:
        print("The number is divisible by 8\n")
    else:
        print("The number is not divisible by 8\n")

if __name__ == '__main__':
    main()

