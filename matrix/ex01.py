from ex00 import scale_vector, add_vectors
import argparse

def linear_combination(vectors, scalars):
    """
    Computes a linear combination of two vectors: a1 * v1 + a2 * v2
    """
    # Scale the vectors by their respective scalars
    temp1 = scale_vector(vectors[0], scalars[0])
    print("Scaled Vector 1:", temp1)  # Optional Debugging
    temp2 = scale_vector(vectors[1], scalars[1])
    print("Scaled Vector 2:", temp2)  # Optional Debugging
    # Add the scaled vectors
    return add_vectors(temp1, temp2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test vector and matrix operations with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Test operations with complex numbers.")
    args = parser.parse_args()

    if args.complex:
        # Test vector operations with complex numbers
        v1 = [1 + 2j, 3 + 4j, 5 + 6j]
        v2 = [6 - 7j, 8 - 9j, 10 - 11j]

    else:
        # Test vector operations
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]

    vectors = [v1, v2]
    scalars = [3, 2]

    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"scalar1: {scalars[0]}")  # Fixed indexing
    print(f"scalar2: {scalars[1]}")  # Fixed indexing
    print("Linear Combination:", linear_combination(vectors, scalars))
