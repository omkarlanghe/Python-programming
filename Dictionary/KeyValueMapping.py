def from_keys(input_dict, value = None):
    result = dict()
    Keys = input_dict.keys()
    if type(value) == list:
        i = 0
        for key in Keys:
            if i < len(value):
                result[key] = value[i]
                i+=1
                continue
            result[key] = None
    else:
        result = dict.fromkeys(input_dict, value)

    return result

def main():
    input_dict = input("Enter the elements in dictionary\n")
    value = input("Enter value\n")

    print("Resultant dictionary with mapping -", from_keys(input_dict, value))

if __name__ == '__main__':
    main()

