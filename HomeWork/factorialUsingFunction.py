def factorial(number):
    result = 1;
    for x in range(2, number+1):
        result = result*x

    return result

number = eval(input("Enter the number:\n"))
print(factorial(number))

