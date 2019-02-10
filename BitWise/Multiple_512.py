def Multiple(number):
    if(number&(511) == 0):
        return True
    else:
        return False

def main():
    number = eval(input("Enter the number to check it's multiple:\n"))

    retVal = Multiple(number)

    if(retVal == True):
        print("It's a multiple of ", number)
    else:
        print("It's not a multiple of ", number)

if __name__ == '__main__':
    main()

