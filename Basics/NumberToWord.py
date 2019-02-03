def ReverseString(number):
    reminder = 0
    result = 0

    while number != 0:
        reminder = number % 10
        result = result * 10 + reminder
        number = int(number//10)

    return result

def NumberToWordConversion(number):
    rem = 0
    result = ReverseString(number)
    
    while result != 0:
        rem = result % 10
        
        if rem == 0:
            print("Zero", end = ' ')
        elif rem == 1:
            print("One", end = ' ')
        elif rem == 2:
            print("Two", end = ' ')
        elif rem == 3:
            print("Three", end = ' ')
        elif rem == 4:
            print("Four", end = ' ')
        elif rem == 5:
            print("Five", end = ' ')
        elif rem == 6:
            print("Six", end = ' ')
        elif rem == 7:
            print("Seven", end = ' ')
        elif rem == 8:
            print("Eight", end = ' ')
        elif rem == 9:
            print("Nine", end = ' ')
                
        result = int(result//10)

def main():
    number = eval(input("Enter the number:\n"))
    NumberToWordConversion(number)
    
if __name__ == '__main__':
    main()
