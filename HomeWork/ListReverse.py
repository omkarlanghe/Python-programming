def ReverseUsingRecursion(input_list):
    if len(input_list) == 0:
        return

    ReverseUsingRecursion(input_list[1:])
    print(input_list[0])

def main():
    input_list = eval(input("Enter elements in the list:\n"))
    ReverseUsingRecursion(input_list)

if __name__ == "__main__":
    main()

