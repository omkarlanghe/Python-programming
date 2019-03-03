#WAP to read file from user and print smallest and longest line from user.

def ReadFileSmallestLongestLine(filename):
    fd = open(filename)
    line = fd.readline()
    max_line = line
    min_line = line

    while line != "":
        line = fd.readline()
        if line == '\n' or line == '':
            continue
        if len(line) > len(max_line):
            max_line = line
        elif len(line) < len(min_line):
            min_line = line
    
    return max_line, min_line

def main():
    maxline,minline = ReadFileSmallestLongestLine(input("Enter File Name:"))
    print("Maxline = {}\nMinLine = {}".format(maxline,minline))

if __name__ == '__main__':
    main()


