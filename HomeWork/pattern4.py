def Pattern(n):
    for i in range(1,n+1):
        ch = 64 + i
        count = 1
        for j in range(1, n-i+1):
            print(' ',end='')

        for j in range(1, 2*i):
            print(chr(ch), end = '')

            if(j < i):
                ch = ch - 1
            else:
                ch = ch + 1
        print()

def main():
    n = eval(input("Enter the number:\n"))
    Pattern(n)

if __name__ == '__main__':
    main()
