def count_words(paragraph):
    result = {}
    for word in paragraph.split():
        if result.get(word) != None:
            result[word] += 1
        else:
            result[word] = 1
    return result

def main():
    paragraph = input("Enter the paragraph\n")
    print("Resultant dictionary -", count_words(paragraph))

if __name__ == '__main__':
    main()

