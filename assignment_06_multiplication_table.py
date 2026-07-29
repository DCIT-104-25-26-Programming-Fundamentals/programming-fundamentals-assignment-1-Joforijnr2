# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================

def print_single_table(number):
    """Print the multiplication table for one number from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number}  x  {multiplier}  =  {result}")


def print_tables_up_to(n):
    """Print multiplication tables for every number from 1 to n."""
    for number in range(1, n + 1):
        print_single_table(number)
        if number < n:
            print("-" * 27)


def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if number <= 0:
        print("Error: N must be a positive integer.")
        return

    print_single_table(number)

    try:
        n = int(input("Enter a number N for tables from 1 to N: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to(n)


if __name__ == "__main__":
    main()

