def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("****** Simple Calculator ******")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        while True:
            next_calc = input("\nDo you want to perform another calculation? (y/n): ").lower()
            if next_calc in ['y' , 'n']:
                break
            else:
                print("Invalid choice ! Please enter y or n.")

        if next_calc.lower() == 'n':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
