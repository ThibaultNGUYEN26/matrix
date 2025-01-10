import argparse

def mul_vec(matrix, vector):
    """
    Multiplies a matrix by a vector.
    """
    # Check if the number of columns in the matrix matches the size of the vector
    if len(matrix[0]) != len(vector):
        raise ValueError("Number of columns in the matrix must match the size of the vector.")

    # Perform the matrix-vector multiplication
    return [
        sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix
    ]


def mul_mat(u, v):
    """
    Multiplies two matrices A and B.
    """
    # Check if matrices are compatible for multiplication
    if len(u[0]) != len(v):
        raise ValueError("Number of columns in A must match the number of rows in B.")

    # Dimensions of the result matrix
    m = len(u)  # Number of rows in A
    p = len(v[0])  # Number of columns in B

    # Perform matrix multiplication
    return [[sum(u[i][k] * v[k][j] for k in range(len(v))) for j in range(p)] for i in range(m)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test matrix-vector and matrix-matrix multiplication with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrix-vector multiplication
        test_cases_vec = [
            ([[1 + 1j, 0], [0, 1 + 1j]], [4 + 2j, 2 - 3j]),
            ([[2 + 2j, 0], [0, 2 + 2j]], [4 - 1j, 2 + 3j]),
            ([[2, -2j], [-2j, 2]], [4 + 1j, 2 - 3j]),
        ]

        # Test cases for complex matrix-matrix multiplication
        test_cases_mat = [
            ([[1 + 1j, 0], [0, 1 + 1j]], [[1 + 1j, 0], [0, 1 + 1j]]),
            ([[1 + 1j, 0], [0, 1 + 1j]], [[2, 1 + 1j], [4, 2]]),
            ([[3, -5j], [6 + 2j, 8]], [[2, 1], [4, 2]]),
        ]

    else:
        # Test cases for real matrix-vector multiplication
        test_cases_vec = [
            ([[1, 0], [0, 1]], [4, 2]),
            ([[2, 0], [0, 2]], [4, 2]),
            ([[2, -2], [-2, 2]], [4, 2]),
        ]

        # Test cases for real matrix-matrix multiplication
        test_cases_mat = [
            ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
            ([[1, 0], [0, 1]], [[2, 1], [4, 2]]),
            ([[3, -5], [6, 8]], [[2, 1], [4, 2]]),
        ]

    for u, v in test_cases_vec:
        print(f"Matrix (u): {u}")
        print(f"Vector (v): {v}")
        try:
            print("Multiply Vector:", mul_vec(u, v))
        except ValueError as e:
            print("Error:", e)
        print()


    for u, v in test_cases_mat:
        print(f"Matrix 1 (u): {u}")
        print(f"Matrix 2 (v): {v}")
        try:
            print("Multiply Matrix:", mul_mat(u, v))
        except ValueError as e:
            print("Error:", e)
        print()
