
def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")


    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = None

    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
        operation = "Division"

    print(f"{operation} result: {result}")

calculator()
