#WAP to accept a file name from user and print all digits from it.

import re

def PrintAllDigits(input_file):
    fd = open(input_file)
    data = fd.read()
    regex_obj = re.compile(r"\d+")
    for match in regex_obj.finditer(data):
        print(match)

def main():
    file_name = input("Enter filename: ")
    PrintAllDigits(file_name)

if __name__ == '__main__':
    main()

'''
#HOMEWORK:
1. WAP to accept a filename from user and delete comments from it.
2. WAP to accept a filename from user and print all the words starting with Capital letters.
'''
