def Pattern(n):
    for i in range(1, n+1):
        count = i
        for j in range(1, n-i+1):
            print(' ', end='')

        for j in range(1, 2*i):
            print(count, end = '')
            
            if(j < i):
                count = count - 1
            else:
                count = count + 1
        print()

def main():
    n = eval(input("Enter the number:\n"))
    Pattern(n)

if __name__ == '__main__':
    main()

