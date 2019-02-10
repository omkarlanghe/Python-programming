def RecursiveFactorial(num):
    if num == 0 or num == 1:
        return 1

    if num == 2:
        return 2

    return num*RecursiveFactorial(num-1)

def main():
    num = eval(input("Enter the number:\n"))
    retVal = RecursiveFactorial(num)
    
    print("Factorial is: ", retVal)

if __name__ == '__main__':
    main()
