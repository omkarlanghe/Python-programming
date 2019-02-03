def TurnOffBits(no, pos, noOfBits):
    
    x = (1<<noOfBits-1)
    x = x<<(pos-noOfBits)
    x = ~x
    no = no&x

    return no

def main():
    number = eval(input("Enter the number:\n"))
    pos = eval(input("Enter the bit position:\n"))
    noOfBits = eval(input("Enter no. of bits to turn off:\n"))

    print("Before turnoff bits: ", number)

    retVal = TurnOffBits(number, pos, noOfBits)
    print("After turnoff bits: ", retVal)

if __name__ == '__main__':
    main()

