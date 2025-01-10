import argparse

def add_vectors(v1, v2):
    """
    Adds two vectors of the same size.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same size.")
    return [v1[i] + v2[i] for i in range(len(v1))]


def subtract_vectors(v1, v2):
    """
    Subtracts two vectors of the same size.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same size.")
    return [v1[i] - v2[i] for i in range(len(v1))]


def scale_vector(v, scalar):
    """
    Multiplies a vector by a scalar.
    """
    return [scalar * v[i] for i in range(len(v))]


def add_matrices(m1, m2):
    """
    Adds two matrices of the same size.
    """
    if len(m1) != len(m2) or any(len(row1) != len(row2) for row1, row2 in zip(m1, m2)):
        raise ValueError("Matrices must be of the same size.")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]


def subtract_matrices(m1, m2):
    """
    Subtracts two matrices of the same size.
    """
    if len(m1) != len(m2) or any(len(row1) != len(row2) for row1, row2 in zip(m1, m2)):
        raise ValueError("Matrices must be of the same size.")
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]


def scale_matrix(m, scalar):
    """
    Multiplies a matrix by a scalar.
    """
    return [[scalar * m[i][j] for j in range(len(m[i]))] for i in range(len(m))]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test vector and matrix operations with real or complex numbers.")
    parser.add_argument("-c", "--complex", action="store_true", help="Test operations with complex numbers.")
    args = parser.parse_args()

    if args.complex:
        # Test vector operations with complex numbers
        v1 = [1 + 2j, 3 + 4j, 5 + 6j]
        v2 = [6 - 7j, 8 - 9j, 10 - 11j]

        # Test matrix operations with complex numbers
        m1 = [
            [1 + 2j, 2 + 3j, 3 + 4j],
            [4 + 5j, 5 + 6j, 6 + 7j]
        ]
        m2 = [
            [7 - 8j, 8 - 9j, 9 - 10j],
            [10 - 11j, 11 - 12j, 12 - 13j]
        ]

    else:
        # Test vector operations with real numbers
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]

        # Test matrix operations with real numbers
        m1 = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        m2 = [
            [7, 8, 9],
            [10, 11, 12]
        ]

    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print("Add vectors (v1 + v2):", add_vectors(v1, v2))
    print("Subtract vectors (v1 - v2):", subtract_vectors(v1, v2))
    print("Scale vector (v1 * 2):", scale_vector(v1, 2))

    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print("Add matrices (m1 + m2):", add_matrices(m1, m2))
    print("Subtract matrices (m1 - m2):", subtract_matrices(m1, m2))
    print("Scale matrix (m1 * 3):", scale_matrix(m1, 3))
