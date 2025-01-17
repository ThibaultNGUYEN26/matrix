from ex10 import row_echelon_form
import argparse

def rank(u):
    """
    Computes the rank of a matrix.
    """
    # Transform to row echelon form
    ref = row_echelon_form(u)

    # Count non-zero rows
    rank = 0
    for row in ref:
        if any(value != 0 for value in row):  # Row has at least one non-zero element
            rank += 1

    return rank


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the rank of a matrix with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrices
        test_cases = [
            ([[1 + 1j, 0, 0], [0, 1 + 1j, 0], [0, 0, 1 + 1j]]),
            ([[1 + 2j, 2 + 1j, 0, 0], [2 + 3j, 4 + 5j, 0, 0], [-1 - 2j, 2 + 1j, 1 + 3j, 1 + 1j]]),
            ([[8 + 1j, 5 - 2j, -2 + 3j], [4 - 1j, 7 + 4j, 20 - 5j], [7 + 2j, 6 - 3j, 1 + 4j], [21 - 2j, 18 + 3j, 7 + 1j]]),
        ]

    else:
        # Test cases for real matrices
        test_cases = [
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            ([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]]),
            ([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]]),
        ]

    for u in test_cases:
        print(f"u: {u}")
        try:
            print("Rank:", rank(u))
        except ValueError as e:
            print("Error:", e)
        print()
