import argparse

def transpose(matrix):
    """
    Computes the transpose of a matrix.
    """
    # Use list comprehension to swap rows and columns
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the transpose of a matrix with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrices
        test_cases = [
            [[1 + 1j, 0], [0, 1 - 1j]],
            [[2 + 2j, -5j, 0], [4 - 1j, 3 + 3j, 7], [-2, 3 + 4j, 4 - 2j]],
            [[-2j, -8 + 1j, 4 - 4j], [1 + 2j, -23j, 4], [0, 6 - 1j, 4 + 3j]]
        ]

    else:
        # Test cases for real matrices
        test_cases = [
            [[1, 0], [0, 1]],
            [[2, -5, 0], [4, 3, 7], [-2, 3, 4]],
            [[-2, -8, 4], [1, -23, 4], [0, 6, 4]]
        ]

    for u in test_cases:
        print(f"Matrix (u): {u}")
        try:
            print("Transpose:", transpose(u))
        except ValueError as e:
            print("Error:", e)
        print()
