import argparse

def linear_interpolation(v1, v2, t):
    """
    Performs linear interpolation between two values, vectors, or matrices.
    v1: First value (int, float, list, or nested list)
    v2: Second value (same type as v1)
    t: Interpolation factor (0 <= t <= 1)
    """
    # Scalars
    if isinstance(v1, (int, float, complex)) and isinstance(v2, (int, float, complex)):
        return v1 + t * (v2 - v1)

    # Vectors
    if isinstance(v1, list) and isinstance(v2, list) and all(isinstance(x, (int, float, complex)) for x in v1):
        if len(v1) != len(v2):
            raise ValueError("Vectors must be of the same size.")
        return [v1[i] + t * (v2[i] - v1[i]) for i in range(len(v1))]

    # Matrices
    if isinstance(v1, list) and isinstance(v2, list) and all(isinstance(row, list) for row in v1):
        if len(v1) != len(v2) or any(len(row1) != len(row2) for row1, row2 in zip(v1, v2)):
            raise ValueError("Matrices must be of the same size.")
        return [
            [v1[i][j] + t * (v2[i][j] - v1[i][j]) for j in range(len(v1[i]))]
            for i in range(len(v1))
        ]

    raise TypeError("Inputs must be scalars, vectors, or matrices of compatible types.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test linear interpolation with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    # Test cases
    if args.complex:
        test_cases = [
            {"a": 0 + 1j, "b": 1 + 2j, "t": 0, "type": "scalar"},
            {"a": 0 + 1j, "b": 1 + 2j, "t": 1, "type": "scalar"},
            {"a": [1 + 1j, 2 + 2j], "b": [3 + 3j, 4 + 4j], "t": 0.5, "type": "vector"},
            {"a": [[1 + 1j, 2 + 2j], [3 + 3j, 4 + 4j]], "b": [[5 + 5j, 6 + 6j], [7 + 7j, 8 + 8j]], "t": 0.5, "type": "matrix"},
        ]

    else:

        test_cases = [
            {"a": 0, "b": 1, "t": 0, "type": "scalar"},
            {"a": 0, "b": 1, "t": 1, "type": "scalar"},
            {"a": [2, 1], "b": [4, 2], "t": 0.3, "type": "vector"},
            {"a": [[2, 1], [3, 4]], "b": [[20, 10], [30, 40]], "t": 0.5, "type": "matrix"},
        ]

    for test in test_cases:
        a = test["a"]
        b = test["b"]
        t = test["t"]
        print(f"Type: {test['type'].capitalize()}")
        print(f"a: {a}")
        print(f"b: {b}")
        print(f"t: {t}")
        try:
            print("Linear Interpolation:", linear_interpolation(a, b, t))
        except ValueError as e:
            print("Error:", e)
        print()
