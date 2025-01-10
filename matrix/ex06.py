import argparse

def cross_product(u, v):
    """
    Computes the cross product of two 3-dimensional vectors u and v.
    """
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Both vectors must be of size 3.")

    return [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the cross product of two 3D vectors. Supports both real and complex vectors.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for the vector calculations.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex vectors
        test_cases = [
            ([1 + 1j, 0 + 0j, 0 + 0j], [0 + 0j, 1 + 1j, 0 + 0j]),
            ([1 + 1j, 2 + 2j, 3 + 3j], [4 + 4j, 5 + 5j, 6 + 6j]),
            ([1 + 2j, -3 + 4j, 5 - 6j], [-7 + 8j, 9 - 10j, -11 + 12j])
        ]

    else:
        # Test cases for real vectors
        test_cases = [
            ([0, 0, 1], [1, 0, 0]),
            ([1, 2, 3], [4, 5, 6]),
            ([4, 2, -3], [-2, -5, 16])
        ]

    for u, v in test_cases:
        print(f"u: {u}")
        print(f"v: {v}")
        try:
            print("Cross product:", cross_product(u, v))
        except ValueError as e:
            print("Error:", e)
        print()
