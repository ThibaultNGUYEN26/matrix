import argparse

def norm_1(vector):
    """
    Computes the 1-norm (Manhattan norm) of a vector.
    """
    return sum(abs(x) for x in vector)


def norm_2(vector):
    """
    Computes the 2-norm (Euclidean norm) of a vector.
    """
    return sum(abs(x)**2 for x in vector)**0.5


def norm_inf(vector):
    """
    Computes the infinity norm (maximum absolute value) of a vector.
    """
    return max(abs(x) for x in vector)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test norm computations with real or complex vectors.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for test cases.")
    args = parser.parse_args()

    if args.complex:
        # Test cases for complex vectors
        test_cases = [
            [0 + 0j, 0 + 0j, 0 + 0j],
            [1 + 1j, 2 + 2j, 3 + 3j],
            [-1 - 1j, -2 - 2j]
        ]

    else:
        # Test cases for real vectors
        test_cases = [
            [0, 0, 0],
            [1, 2, 3],
            [-1, -2]
        ]

    for vector in test_cases:
        print(f"vector: {vector}")
        try:
            print(f"norm_1: {norm_1(vector)} | norm_2: {norm_2(vector)} | norm_inf: {norm_inf(vector)}")
        except ValueError as e:
            print("Error:", e)
        print()
