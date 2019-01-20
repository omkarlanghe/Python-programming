#WAP to accept senetence from user and replace the 'not bad' construct if found with 'good'
#!user/bin/python

input_stmt = (input("Enter the sentence:\n"))
not_index = input_stmt.find("not")
if(not_index != -1):
    bad_index = input_stmt.find("bad")
    if(bad_index != -1 and bad_index > not_index):
        result = input_stmt[:not_index]
        result += 'good'
        result += input_stmt[bad_index+3:]
print(result)

