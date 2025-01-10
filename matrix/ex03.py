import argparse

def dot(u, v):
    """
    Computes the dot product of two vectors u and v.
    """
    if len(u) != len(v):
        raise ValueError("Vectors must be of the same length.")
    return sum(u[i] * v[i] for i in range(len(u)))


def dot_complex(u, v):
    """
    Computes the dot product of two complex vectors u and v.
    """
    if len(u) != len(v):
        raise ValueError("Vectors must be of the same length.")
    return sum(u[i] * v[i].conjugate() for i in range(len(u)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test dot product computation with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex vectors
        test_cases = [
            ([0 + 0j, 0 + 0j], [1 + 1j, 1 - 1j]),
            ([1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]),
            ([-1 - 2j, 6 + 1j], [3 + 3j, 2 - 2j])
        ]

        for u, v in test_cases:
            print(f"u: {u}")
            print(f"v: {v}")
            try:
                print("Dot:", dot_complex(u, v))
            except ValueError as e:
                print("Error:", e)
            print()

    else:
        # Test cases
        test_cases = [
            ([0, 0], [1, 1]),
            ([1, 1], [1, 1]),
            ([-1, 6], [3, 2])
        ]

        for u, v in test_cases:
            print(f"u: {u}")
            print(f"v: {v}")
            try:
                print("Dot:", dot(u, v))
            except ValueError as e:
                print("Error:", e)
            print()
