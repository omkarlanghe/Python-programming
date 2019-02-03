def ArithmeticOperation():
    choice = 0

    while choice != 5:
        choice = Menu()

        num1 = eval(input("Enter 1st number:\n"))
        num2 = eval(input("Enter 2nd number:\n"))

        if choice == 1:
            addition = num1 + num2
            print("Addition of two numbers is ->", addition)
            print()
        elif choice == 2:
            subtraction = num1 - num2
            print("Subtraction of two numbers is ->", subtraction)
            print()
        elif choice == 3:
            multiplication = num1 * num2
            print("Multiplication of two numbers is ->", multiplication)
            print()
        elif choice == 4:
            division = int(num1//num2)
            print("Division of two numbers is ->", division)
            print()
        elif choice == 5:
            return 0
        else:
            return -1

def Menu():
    while True:
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")

        choice = int(input("Enter choice:\n"))
        if (choice > 0 and choice < 6):
            return choice

def main():
    ArithmeticOperation()

if __name__ == '__main__':
    main()
    
