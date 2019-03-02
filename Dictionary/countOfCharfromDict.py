def dictionary_of_chars(sentence):
    result = {}
    for ch in sentence:
        if result.get(ch) != None:
            result[ch]+=1
        else:
            result[ch] = 1
    return result


def main():
    sentence = input("Enter sentence:\n")
    result = dictionary_of_chars(sentence)
    print("Resultant dictionary is -", result)

if __name__ == '__main__':
    main()

