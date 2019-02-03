#   *
#  ***
# *****
#*******

def Pattern(n):
    for i in range(1,n+1):
        for _ in range(1, n-i+1):
            print(' ',end='')

        for _ in range(1, i*2):
            print('*',end='')

        print()

def main():
    n = eval(input("Enter number:\n"))
    Pattern(n)

if __name__ == '__main__':
    main()


