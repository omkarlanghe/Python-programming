#WAP to accept filename from user and print those line which have "The" more than once.

def WordMoreThanOnce(filename, searchWord):
    fd = open(filename)
    line = fd.readline()
    count = 0
    while line != "":
        for word in line.split():
            if word == searchWord:
                count += 1
                if count > 1:
                    print(line)
                    break
                else:
                    continue
        
        line = fd.readline()
    print()
def main():
    filename = input("Enter name of the file: ")
    searchWord = input("Enter the word to search in the given line: ")
    WordMoreThanOnce(filename, searchWord)

if __name__ == '__main__':
    main()
