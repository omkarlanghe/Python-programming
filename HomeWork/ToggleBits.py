def ToggleBits(no, pos, noOfBits):
    x = 1<<(noOfBits)-1
    x = x<<(pos-noOfBits)

    return no^x

def main():
    no = eval(input("Enter the number:\n"))
    pos = eval(input("Enter position to enter:\n"))
    noOfBits = eval(input("Enter number of bits to toggle:\n"))

    print("Number before toggle:\n", no)
    print("Binary = ", bin(no)) 

    retVal = ToggleBits(no, pos, noOfBits)
    print("Number after toggle:\n", retVal)
    print("Binary = ",bin(retVal))
    
if __name__ == '__main__':
    main()


