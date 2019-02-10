def SwapBits(x, y, posx, bits):
    mask = (1<<bits)-1 #..000000001111
    mask = mask<<(posx-bits) #00001111000

    x_part = x&mask #00001101000
    y_part = y&mask #..0001010000

    x = x&~mask
    y = y&~mask

    x = x|y_part
    y = y|x_part

    return x,y

def SwapBitsGeneric(x,y,posx, posy,bits):
    mask = (1<<bits)-1

    xmask = mask<<(posx - bits)
    ymask = mask<<(posy - bits)


    x_part = x&xmask
    y_part = y&ymask

    if(posx > posy):
        x_part = x_part>>(posx-posy)
        y_part = y_part<<(posx-posy)
    else:
        x_part = x_part<<(posy-posx)
        y_part = y_part>>(posy-posx)


    x = x&~xmask
    y = y&~ymask

    return x|x_part,y|y_part

def main():
    x = eval(input("Enter first number:\n"))
    y = eval(input("Enter second number:\n"))
    
    posx = eval(input("Enter position:\n"))
    posy = eval(input("Enter position:\n"))

    bits = eval(input("Enter bits to swap:\n"))

    print("x and y part after swapping is: ", SwapBits(x,y,posx,bits))
    print("x and y part after swapping is: ", SwapBitsGeneric(x,y,posx,posy,bits))

if __name__ == '__main__':
    main()

