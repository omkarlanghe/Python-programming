def SwapBits(num1, num2, posx, bits):
    mask = (1<<bits)-1 #..000000001111
    mask = mask<<(posx-bits) #00001111000

    x_part = num1&mask #00001101000
    y_part = num2&mask #..0001010000

    num1 = num1&(~mask)
    num2 = num2&(~mask)

    num1 = num1|y_part
    num2 = num2|x_part

    return num1,num2

def SwapBitsGeneric(num1,num2,pos1, pos2,noOfBits):
    temp=1
    temp=(temp<<noOfBits)-1
    temp1=temp<<(pos1-noOfBits)
    temp2=temp<<(pos2-noOfBits)
	
    x_part=(num1 & temp1) >> (pos1-noOfBits)
    y_part=(num2 & temp2) >> (pos2-noOfBits)
    
    x_part=x_part << (pos2-noOfBits)
    y_part=y_part << (pos1-noOfBits)
    	
    num1=num1 & (~temp1)
    num2=num2 & (~temp2)
    	
    x_swapped=y_part | num1
    y_swapped=x_part | num2	
    
    return x_swapped,y_swapped

def main():
    num1 = eval(input("Enter first number:\n"))
    num2 = eval(input("Enter second number:\n"))
    
    posx = eval(input("Enter position for 1st number:\n"))
    posy = eval(input("Enter position for 2nd number:\n"))

    bits = eval(input("Enter bits to swap:\n"))

    print("(Same Position) x and y part after swapping is: ", SwapBits(num1,num2,posx,bits))
    print("(Different Position) x and y part after swapping is: ", SwapBitsGeneric(num1,num2,posx,posy,bits))

if __name__ == '__main__':
    main()

