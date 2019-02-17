def ReverseContainer(input_list):
    if len(input_list) == 0:
        if type(input_list) == str:
            return input_list

        return list()

    x = ReverseContainer(input_list[1:])

    if type(x) == str:
        return x + input_list[0]
    x.append(input_list[0])
    return x

def main():
    input_list = eval(input("enter the elements"))

    print(ReverseContainer(input_list))

if __name__ == "__main__":
    main()

