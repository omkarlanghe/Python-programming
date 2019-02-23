def bubblesort(l1):
    i = 0
    for i in range(len(l1)):
        already_sorted = True
        for j in range(len(l1)-i-1):
            if l1[j] > l1[j+1]:
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp
        temp = temp - 1
    return l1

def main():
    l1 = eval(input("Enter the elements in the list:\n"))
    print(bubblesort(l1))

if __name__ == "__main__":
    main()

