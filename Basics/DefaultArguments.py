def Addition(a , b, c = 0, d = 0, e = 0):
    return a+b+c+d+e

def Multiplication(a, b, c = 1, d = 1, e = 1):
    return a*b*c*d*e

def main():
    retVal1 = Addition(10,20)
    retVal2 = Addition(10,20,30,40,50)
    retVal3 = Multiplication(10,20)
    retVal4 = Multiplication(10,20,30,40,50)

    print("Addition is: ",retVal1)
    print("Addition is: ",retVal2)
    print("Multiplication is: ",retVal3)
    print("Multiplication is: ",retVal4)

if __name__ == '__main__':
    main()
