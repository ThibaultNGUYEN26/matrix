import argparse

def row_echelon_form(u):
    """
    Transforms a matrix into reduced row echelon form using Gaussian elimination.
    """
    rows = len(u)
    cols = len(u[0])
    lead = 0  # Track the leading column (pivot column)

    for r in range(rows):
        if lead >= cols:
            break

        # Step 1: Ensure the pivot is non-zero, swap rows if necessary
        i = r
        while u[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return u

        # Swap rows if necessary
        u[r], u[i] = u[i], u[r]

        # Step 2: Normalize the pivot row (set the pivot to 1)
        pivot = u[r][lead]
        u[r] = [x / pivot for x in u[r]]

        # Step 3: Eliminate all entries in the column above and below the pivot
        for i in range(rows):
            if i != r:
                factor = u[i][lead]
                u[i] = [u[i][k] - factor * u[r][k] for k in range(cols)]

        lead += 1

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
            print("Row Echelon:", row_echelon_form(u))
        except ValueError as e:
            print("Error:", e)
        print()
