def PrintCountOfConsonants(input_string):
    count = 0
    for x in input_string:
        if x != 'aeiouAEIOU':
            continue
        else:
            count = count+1
    return count

def main():
    input_string = input("Enter the string:\n")

    retVal = PrintCountOfConsonants(input_string)
    print("Count of consonants is: ", retVal)

if __name__ == '__main__':
    main()

