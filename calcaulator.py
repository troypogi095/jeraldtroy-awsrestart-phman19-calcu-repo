def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("Result: ", result)
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    calculator()
