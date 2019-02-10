def CountOneBits(no):
    count = 0
    while(no != 0):
        count += 1
        no = no&(no-1)

    return count

def CountZeroBits(no):
    count = 0
    x = 1
    
    while(x<=no):
        if((no&x)!=1):
            count += 1
            
        x = x<<1

    return count

def main():
    no = eval(input("Enter the number:\n"))

    oneBits = CountOneBits(no)
    zeroBits = CountZeroBits(no)

    print("Count of one bits is: ",oneBits)
    print("Count of zero bits is: ", zeroBits)
    
    
if __name__ == '__main__':
    main()

