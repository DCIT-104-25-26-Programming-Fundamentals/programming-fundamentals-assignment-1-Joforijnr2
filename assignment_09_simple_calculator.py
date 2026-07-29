# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# Topic: Console Calculators and Functions
# =============================================================================

def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus_numbers(a, b):
    if b == 0:
        return None
    return a % b


def power_numbers(a, b):
    return a ** b


def main():
    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choice == "1":
            result = add_numbers(first_number, second_number)
            print(f"Result: {first_number} + {second_number} = {result}")
        elif choice == "2":
            result = subtract_numbers(first_number, second_number)
            print(f"Result: {first_number} - {second_number} = {result}")
        elif choice == "3":
            result = multiply_numbers(first_number, second_number)
            print(f"Result: {first_number} * {second_number} = {result}")
        elif choice == "4":
            result = divide_numbers(first_number, second_number)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first_number} / {second_number} = {result}")
        elif choice == "5":
            result = modulus_numbers(first_number, second_number)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first_number} % {second_number} = {result}")
        elif choice == "6":
            result = power_numbers(first_number, second_number)
            print(f"Result: {first_number} ** {second_number} = {result}")
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()

