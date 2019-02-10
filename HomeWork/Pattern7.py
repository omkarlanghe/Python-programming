def PatternDouble(n):
    for i in range(1,n+1):
        k = i;
        for _ in range(1, i+2):
            print(k, end = ' ')
            k *= 2
        print()

def PatternTri(n):
    for i in range(1,n+1):
        k = i
        for _ in range(1, i+2):
            print(k, end = ' ')
            k += i

        print()

def PatternSandwitch(n):
    for i in range(1,n+1):
        
        for j in range(1, n-i+1):
            k = n-j
            print(k, end = ' ')
            

        for _ in range(1,i+1):
            print("*", end = ' ')
        print()

def PatternArrow(n):
    for i in range(1, n+1):
        count = i
        for j in range(1, i+1):
            if j<=i:
                print(count, end = ' ')
                count = count + 1
            

        print()

def main():
    n = eval(input("Enter the number:\n"))
    PatternDouble(n)
    print()
    PatternTri(n)
    print()
    PatternSandwitch(n)
    print()
    PatternArrow(n)

if __name__ == '__main__':
    main()

