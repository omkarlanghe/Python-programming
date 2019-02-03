

#   *
#  **
# ***
#****

def Pattern(number):
    for i in range(1, number+1):
        for _ in range(1,number-i+1):
            print(' ',end='')

        for _ in range(1,i+1):
            print('*', end='')

        print()



def main():
    number = eval(input("Enter number:\n"))
    Pattern(number)

if __name__ == '__main__':
    main()
