def TurnOnBits(no, pos, noOfBits):
    
    x = (1<<noOfBits-1)
    x = x<<pos-noOfBits
    no = no|x

    return no

def main():
    no = eval(input("Enter the number to check:\n"))
    pos = eval(input("Enter bit position:\n"))
    noOfBits = eval(input("Enter number of bits to turn on:\n"))

    print("Before turnOn: ", no)

    retVal = TurnOnBits(no, pos, noOfBits)
    print("After turnOn:", retVal)

if __name__ == '__main__':
    main()

