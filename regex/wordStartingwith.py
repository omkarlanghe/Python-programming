#WAP to accept a file name from user and print all the words starting with small or capital 't' and ending in small or capital 'e'
import re

def PrintWordsStartingTEndingE(input_file):
    fd = open(input_file)
    data = fd.read()
    regex_obj = re.compile(r"\bT\w+e\b", re.IGNORECASE) #starting with t and ending with t
    for match in regex_obj.finditer(data):
        print(match)

def main():
    file_name = input("Enter filename: ")
    PrintWordsStartingTEndingE(file_name)

if __name__ == '__main__':
    main()

'''
#HOMEWORK: 
1. WAP to accept a file name from in user and print all verbs in it.
2. WAP to accept a file name from user and print all words having 'e' and 'd' in between. (eg: jeetendra)
3. WAP to accept a file name from user and print all digits from it.
'''
