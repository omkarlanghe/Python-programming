#WAP to accept filename from user and print those lines who has < or = 80 characters. Also print line numbers which have more than 80 characters, stating that line having more than standard count of character.

def ReadFileLessThan80Chars(filename):
    fd = open(filename)
    line_numbers = []
    line_no = 1
    if fd != None:
        line = fd.readline()
        while line != "":
            if len(line) <= 10:
                print(line)
            else:
                line_numbers.append(line_no)
            line_no += 1
            line = fd.readline()
        print("Line numbers of lines having more than 80 characters are -> ", line_numbers)

def main():
    filename = input("Enter the name of the file\n")
    ReadFileLessThan80Chars(filename)

if __name__ == '__main__':
    main()

