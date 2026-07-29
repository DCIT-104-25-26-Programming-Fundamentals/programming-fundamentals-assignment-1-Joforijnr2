# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

def print_fibonacci_terms(n):
    """Print the first n Fibonacci numbers on one line."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", end=" ")
    for i, value in enumerate(sequence):
        if i > 0:
            print(end=" ")
        print(value, end="")
    print()


def is_fibonacci_number(number):
    """Return True if the number is a Fibonacci number, otherwise False."""
    if number < 0:
        return False

    a, b = 0, 1
    while a < number:
        a, b = b, a + b

    return a == number


def main():
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    print_fibonacci_terms(n)

    try:
        check_number = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci_number(check_number):
        print(f"{check_number} is a Fibonacci number.")
    else:
        print(f"{check_number} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

