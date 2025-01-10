from ex09 import transpose
from ex11 import determinant
import argparse

def cofactor(u):
    """
    Computes the cofactor matrix of a square matrix.
    """
    n = len(u)
    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [u[x][:j] + u[x][j + 1:] for x in range(n) if x != i]
            cofactor = (-1) ** (i + j) * determinant(minor)
            row.append(cofactor)
        cofactors.append(row)
    return cofactors


def inverse(u):
    """
    Computes the inverse of a square matrix.
    """
    det = determinant(u)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    cofactors = cofactor(u)
    adjugate = transpose(cofactors)
    # Compute the inverse by dividing adjugate by determinant
    return [[adjugate[i][j] / det for j in range(len(u))] for i in range(len(u))]


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
