# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

def read_matrix(rows, cols, matrix_name="matrix"):
    """Read a matrix from user input using the expected row-by-row format."""
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ").strip()
        parts = row_input.split()
        if len(parts) != cols:
            print(f"Error: Each row must contain exactly {cols} values.")
            return None

        row = []
        for part in parts:
            try:
                value = int(part)
            except ValueError:
                print("Error: Matrix values must be integers.")
                return None
            row.append(value)
        matrix.append(row)

    return matrix


def transpose(matrix):
    """Return the transpose of a matrix."""
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for r in range(rows):
        row_sum = []
        for c in range(cols):
            row_sum.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(row_sum)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product of A × B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for i in range(rows_a):
        result_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result_row.append(total)
        result.append(result_row)
    return result


def print_matrix(matrix, title=None):
    """Print a matrix in a neat aligned grid format."""
    if title:
        print(title)

    if not matrix:
        print("[]")
        return

    width = 0
    for row in matrix:
        for value in row:
            width = max(width, len(str(value)))

    for row in matrix:
        line = " ".join(str(value).rjust(width) for value in row)
        print(line)


def read_dimensions(prompt_rows="Enter number of rows: ", prompt_cols="Enter number of columns: "):
    """Read matrix dimensions and return (rows, cols) if valid."""
    try:
        rows = int(input(prompt_rows))
        cols = int(input(prompt_cols))
    except ValueError:
        print("Error: Rows and columns must be integers.")
        return None

    if rows <= 0 or cols <= 0:
        print("Error: Rows and columns must be positive integers.")
        return None

    return rows, cols


def main():
    # Part A — Transpose a Matrix
    dims = read_dimensions()
    if dims is None:
        return
    rows, cols = dims

    matrix = read_matrix(rows, cols, "original matrix")
    if matrix is None:
        return

    transposed_matrix = transpose(matrix)

    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed_matrix)

    # Part B — Add Two Matrices
    print("\n--- Matrix Addition ---")
    dims = read_dimensions()
    if dims is None:
        return
    rows, cols = dims

    print("Enter values for matrix A:")
    matrix_a = read_matrix(rows, cols, "matrix A")
    if matrix_a is None:
        return

    print("Enter values for matrix B:")
    matrix_b = read_matrix(rows, cols, "matrix B")
    if matrix_b is None:
        return

    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nSum Matrix:")
    print_matrix(sum_matrix)

    # Part C — Multiply Two Matrices
    print("\n--- Matrix Multiplication ---")
    dims_a = read_dimensions("Enter number of rows for matrix A: ", "Enter number of columns for matrix A: ")
    if dims_a is None:
        return
    rows_a, cols_a = dims_a

    dims_b = read_dimensions("Enter number of rows for matrix B: ", "Enter number of columns for matrix B: ")
    if dims_b is None:
        return
    rows_b, cols_b = dims_b

    if cols_a != rows_b:
        print("Error: Number of columns in matrix A must equal number of rows in matrix B.")
        return

    print("Enter values for matrix A:")
    matrix_a = read_matrix(rows_a, cols_a, "matrix A")
    if matrix_a is None:
        return

    print("Enter values for matrix B:")
    matrix_b = read_matrix(rows_b, cols_b, "matrix B")
    if matrix_b is None:
        return

    product_matrix = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct Matrix (A × B):")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()

