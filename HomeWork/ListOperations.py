def Merge(list1, list2):
    result = []
    i = 0
    j = 0

    while i<len(list1):
        result.append(list1[i])
        i += 1

    while j<len(list2):
        result.append(list2[j])
        j += 1
    
    return sort(result)

def sort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)-i-1):
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp

    return input_list

def Union(list1, list2):
    i = 0
    j = 0
    result = []
    while(i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list2[j])
            j += 1
            i += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

def Intersect(list1, list2):
    result = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                result.append(list1[i])
                break

    return result

def SymmetricDifference(list1, list2):
    result = []
    i = 0
    j = 0

    while(i < len(list1) and j < len(list2)):
        if(list1[i] != list2[j]):
            result.append(list1[i])
            result.append(list2[j])
            i += 1
            j += 1
            continue
        elif list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
            break
    return result

def main():
    list1 = eval(input("Enter the elements in list 1:\n"))
    list2 = eval(input("Enter the elements in list 2:\n"))
    
    print("Merging of list is: ", Merge(list1, list2))
    print("Intersection of list is: ", Intersect(list1, list2))
    print("Union of list is:", Union(list1, list2))
    print("Symmetric difference is: ", SymmetricDifference(list1, list2))
    #Union(Merge(list1,list2))

if __name__ == "__main__":
    main()
