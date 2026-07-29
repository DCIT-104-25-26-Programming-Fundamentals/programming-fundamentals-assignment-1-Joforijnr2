# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of the numbers without using built-in sum()."""
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    """Return the average of the numbers."""
    if not numbers:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    """Return the maximum value without using built-in max()."""
    if not numbers:
        return None
    current_max = numbers[0]
    for value in numbers[1:]:
        if value > current_max:
            current_max = value
    return current_max


def find_min(numbers):
    """Return the minimum value without using built-in min()."""
    if not numbers:
        return None
    current_min = numbers[0]
    for value in numbers[1:]:
        if value < current_min:
            current_min = value
    return current_min


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Invalid number of values.")
        return

    if count <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        try:
            value = float(input(f"Enter number {i}: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
            return
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_max(numbers)
    minimum = find_min(numbers)

    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()

