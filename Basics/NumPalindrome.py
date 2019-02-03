def Palindrome(number):
    result = 0
    reminder = 0

    while number != 0:
        reminder = number%10
        result = result*10+reminder
        number = int(number//10)

    return result

def main():
    number = eval(input("Enter the number:\n"))
    result = Palindrome(number)
    if(number == result):
        print("Number is palindrome:\n")
    else:
        print("Number is not palindrome:\n")

if __name__ == '__main__':
    main()
