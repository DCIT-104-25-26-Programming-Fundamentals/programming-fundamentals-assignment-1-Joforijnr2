# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================

def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def main():
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is NOT a prime number.")


if __name__ == "__main__":
    main()

