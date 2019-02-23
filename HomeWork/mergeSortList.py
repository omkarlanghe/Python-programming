def sort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)-i-1):
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp

    return input_list

def merge(list1,list2):
    result = []
    i = 0
    j = 0
    while(i<len(list1) and j<len(list2)):

        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[i])
            j += 1

    if(i<len(list1)):
        result.extend(list1[i:])
    if(j<len(list2)):
        result.extend(list2[j:])

    print("sorted list with merge sort", result)

def main():
    list1 = eval(input("Enter the elements in list 1:\n"))
    list2 = eval(input("Enter the elements in list 2:\n"))

    print("sorted list 1 - ", sort(list1))
    print("sorted list 2 - ", sort(list2))

    merge(list1, list2)

if __name__ == "__main__":
    main()

