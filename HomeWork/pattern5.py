def Pattern(n):
    for i in range(1, n+1):
        for _ in range(1,n+1):
            print('*', end='')
        print()

def main():
    n = eval(input("Enter the number:\n"))
    Pattern(n)

if __name__ == '__main__':
    main()

