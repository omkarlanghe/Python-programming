#WAP to accept filename from user and print line by line
#!/usr/bin/python
#import io

def ReadFile(filename):
    fd = open(filename)
    if fd != None:
        line = fd.readline()
        while line != "":
            print(line)
            line = fd.readline()

def main():
    filename = input("Enter the name of the file\n")
    ReadFile(filename)

if __name__ == '__main__':
    main()

