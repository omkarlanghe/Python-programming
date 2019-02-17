def StringLength(input_string):
    count = 0;

    for _ in range(len(input_string)):
        count+=1

    return count

def main():
    input_string = input("Enter the string:\n")
    retVal = StringLength(input_string)
    print("length of the given string is: ", retVal)
    
if __name__ == "__main__":
    main()

