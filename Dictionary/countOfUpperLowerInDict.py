def countofLowerCase(sentence):
    result = {}
    count = 0
    for ch in sentence:
        if ch.islower() == True:
            if result.get(ch) != None:
                result[ch] += 1
            else:
                result[ch] = 1

    return result

def countofUpperCase(sentence):
    result = {}
    count = 0
    for ch in sentence:
        if ch.isupper() == True:
            if result.get(ch) != None:
                result[ch] += 1
            else:
                result[ch] = 1

    return result

def main():
    sentence = input("Enter sentence:\n")
    lowerCase = countofLowerCase(sentence)
    upperCase = countofUpperCase(sentence)

    print("Resultant dictionary for lower case count is - ", lowerCase)
    print("Resultant dictionart for upper case count is - ", upperCase)

if __name__ == '__main__':
    main()

