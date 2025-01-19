# from ex09 import transpose
# from ex11 import determinant
import argparse
import numpy as np

# def cofactor(u):
#     """
#     Computes the cofactor matrix of a square matrix.
#     """
#     n = len(u)
#     cofactors = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             minor = [u[x][:j] + u[x][j + 1:] for x in range(n) if x != i]
#             cofactor = (-1) ** (i + j) * determinant(minor)
#             row.append(cofactor)
#         cofactors.append(row)
#     return cofactors


# def inverse(u):
#     """
#     Computes the inverse of a square matrix.
#     """
#     det = determinant(u)
#     if det == 0:
#         raise ValueError("Matrix is singular and cannot be inverted.")

#     cofactors = cofactor(u)
#     adjugate = transpose(cofactors)
#     # Compute the inverse by dividing adjugate by determinant
#     return [[adjugate[i][j] / det for j in range(len(u))] for i in range(len(u))]

def inverse(u):
    """
    Computes the inverse of a square matrix using Gaussian elimination,
    reducing the time complexity to O(n^3).

    Args:
        u (list of lists): Square matrix.

    Returns:
        list of lists: Inverse of the matrix if it exists.
    """
    n = len(u)
    # Augment the matrix with the identity matrix
    augmented = [row + identity_row for row, identity_row in zip(u, np.identity(n).tolist())]

    # Perform row operations to convert to reduced row echelon form
    for col in range(n):
        # Pivot selection (partial pivoting for numerical stability)
        pivot_row = max(range(col, n), key=lambda i: abs(augmented[i][col]))
        if abs(augmented[pivot_row][col]) < 1e-10:
            raise ValueError("Matrix is singular and cannot be inverted.")

        # Swap rows if needed
        augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]

        # Normalize pivot row
        pivot = augmented[col][col]
        augmented[col] = [x / pivot for x in augmented[col]]

        # Eliminate other rows
        for row in range(n):
            if row != col:
                factor = augmented[row][col]
                augmented[row] = [augmented[row][j] - factor * augmented[col][j] for j in range(2 * n)]

    # Extract the inverse matrix from the augmented matrix
    inverse_matrix = [row[n:] for row in augmented]
    return inverse_matrix


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the inverse of a matrix with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrices
        test_cases = [
            ([[1 + 1j, 0, 0], [0, 1 + 1j, 0], [0, 0, 1 + 1j]]),
            ([[2 + 2j, 0, 0], [0, 2 + 2j, 0], [0, 0, 2 + 2j]]),
            ([[8 + 1j, 5 - 2j, -2 + 3j], [4 - 1j, 7 + 4j, 20 - 5j], [7 + 2j, 6 - 3j, 1 + 4j]])
        ]

    else:
        # Test cases for real matrices
        test_cases = [
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            ([[2, 0, 0], [0, 2, 0], [0, 0, 2]]),
            ([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
        ]

    for u in test_cases:
        print(f"u: {u}")
        try:
            print("Inverse:", inverse(u))
        except ValueError as e:
            print("Error:", e)
        print()
