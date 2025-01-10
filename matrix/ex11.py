import argparse

def determinant(u):
    """
    Computes the determinant of a square matrix.
    """
    # Check if the matrix is square
    if len(u) != len(u[0]):
        raise ValueError("u must be square.")

    # Base case: 1x1 u
    if len(u) == 1:
        return u[0][0]

    # Base case: 2x2 u
    if len(u) == 2:
        return u[0][0] * u[1][1] - u[0][1] * u[1][0]

    # Recursive case: Expansion by minors
    det = 0
    for col in range(len(u)):
        # Minor u
        minor = [row[:col] + row[col + 1:] for row in u[1:]]
        # Compute determinant recursively
        det += (-1)**col * u[0][col] * determinant(minor)

    return det


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the determinant of a matrix with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrices
        test_cases = [
            ([[1 + 1j, -1 - 1j], [-1 + 1j, 1 - 1j]]),
            ([[2 + 2j, 0, 0], [0, 2 - 2j, 0], [0, 0, 2 + 0j]]),
            ([[8 + 1j, 5 - 2j, -2 + 3j], [4 - 1j, 7 + 4j, 20 - 5j], [7 + 2j, 6 - 3j, 1 + 4j]]),
            ([[8 + 1j, 5 + 2j, -2 - 1j, 4 - 4j], [4 + 2j, 2.5 - 3j, 20 + 5j, 4 + 4j], [8 - 2j, 5 + 1j, 1 - 1j, 4 - 3j], [28 + 3j, -4 - 4j, 17 + 2j, 1 - 5j]])
        ]


    else:
        # Test cases for real matrices
        test_cases = [
        ([[1, -1], [-1, 1]]),
        ([[2, 0, 0], [0, 2, 0], [0, 0, 2]]),
        ([[8, 5, -2], [4, 7, 20], [7, 6, 1]]),
        ([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
    ]

    for u in test_cases:
        print(f"Matrix (u): {u}")
        try:
            print("Determinant:", determinant(u))
        except ValueError as e:
            print("Error:", e)
        print()
