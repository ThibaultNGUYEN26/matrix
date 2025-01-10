import argparse

def row_echelon(u):
    """
    Transforms a matrix into row echelon form using Gaussian elimination.
    """
    rows = len(u)
    cols = len(u[0])
    for i in range(min(rows, cols)):  # Pivot index can't exceed matrix dimensions
        # Step 1: Ensure the pivot is non-zero, swap rows if necessary
        if u[i][i] == 0:
            for j in range(i + 1, rows):
                if u[j][i] != 0:
                    u[i], u[j] = u[j], u[i]
                    break

        # Step 2: Normalize the pivot row
        if u[i][i] != 0:
            u[i] = [x / u[i][i] for x in u[i]]

        # Step 3: Eliminate entries below the pivot
        for j in range(i + 1, rows):
            if u[j][i] != 0:
                factor = u[j][i]
                u[j] = [u[j][k] - factor * u[i][k] for k in range(cols)]

    return u

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the Row Echelon Form of a matrix with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex matrices
        test_cases = [
            [[1 + 1j, 0, 0], [0, 1 + 2j, 0], [0, 0, 1 + 3j]],
            [[1 + 1j, 2], [3 + 3j, 4 + 4j]],
            [[1 + 1j, 2], [2 + 2j, 4 + 4j]],
            [[8 + 1j, 5 + 2j, -2 + 3j, 4, 28], [4, 2.5 + 1j, 20, 4, -4], [8, 5, 1 + 2j, 4, 17]],
        ]

    else:
        # Test cases for real matrices
        test_cases = [
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[1, 2], [3, 4]],
            [[1, 2], [2, 4]],
            [[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]],
        ]

    for u in test_cases:
        print(f"u: {u}")
        try:
            print("Row Echelon:", row_echelon(u))
        except ValueError as e:
            print("Error:", e)
        print()
