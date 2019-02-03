def TurnOffSingleBit(number, position):

    x = 1
    x = x<<(position-1)
    x = ~x
    number =  number&x

    return number

def main():
    number = eval(input("Enter the number:\n"))
    position = eval(input("Enter the bit position:\n"))
    print("Befor TurnOff:", number)
    retVal = TurnOffSingleBit(number, position)
    print("After TurnOff: ", retVal)

if __name__ == '__main__':
    main()

