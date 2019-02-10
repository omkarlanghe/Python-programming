def GCD(num1, num2):
    while(num1 != num2):
        if(num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return num1

def RecursiveGCD(num1, num2):

    if num1 == num2:
        return num1
    
    if (num1 > num2):
        return RecursiveGCD(num1-num2, num2)
    return RecursiveGCD(num1, num2-num1)

def main():

    num1 = eval(input("Enter num1:\n"))
    num2 = eval(input("Enter num2:\n"))

    retVal = GCD(num1,num2)
    retValRecursive = RecursiveGCD(num1, num2)

    print("GCD is: ",retVal)
    print("GCD using recursion is: ", retValRecursive)

if __name__ == '__main__':
    main()

