def fibonnaciSeries(n):
    a = 1
    b = 1
    print(a,b, end = ' ')
    n = n - 2
    for i in range(1,n):
        c = a + b
        print(c, end = ' ')
        a = b
        b = c
        n = n - 1

def main():
    n = eval(input("Enter number:\n"))
    retval = fibonnaciSeries(n)

if __name__ == '__main__':
    main()

