from ex03 import dot, dot_complex
from ex04 import norm_2
import argparse

def angle_cos(u, v):
    """
    Computes the cosine of the angle between two vectors u and v.
    """
    # Compute the dot product
    dot_product = dot(u, v)
    norm_2_u = norm_2(u)
    norm_2_v = norm_2(v)

    # Avoid division by zero
    if norm_2_u == 0 or norm_2_v == 0:
        raise ValueError("One or both vectors are zero vectors, cosine is undefined.")

    # Compute the cosine
    return round(dot_product / (norm_2_u * norm_2_v), 10)


def angle_cos_complex(u, v):
    """
    Computes the cosine of the angle between two vectors u and v.
    """
    # Compute the dot product
    dot_product = dot_complex(u, v)
    norm_2_u = norm_2(u)
    norm_2_v = norm_2(v)

    # Avoid division by zero
    if norm_2_u == 0 or norm_2_v == 0:
        raise ValueError("One or both vectors are zero vectors, cosine is undefined.")

    # Compute the cosine
    return dot_product / (norm_2_u * norm_2_v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the cosine of the angle between two vectors. Supports both real and complex vectors.")
    parser.add_argument("-c", "--complex", action="store_true", help="Use complex numbers for the vector calculations.")
    args = parser.parse_args()

    if args.complex:
        # Test cases
        test_cases = [
            ([1 + 1j, 0 + 0j], [1 + 1j, 0 + 0j]),                # Parallel vectors
            ([1 + 1j, 0 + 0j], [0 + 0j, 1 + 1j]),                # Orthogonal vectors
            ([-1 -1j, 1 + 1j], [1 + 1j, -1 - 1j]),               # Opposite direction vectors
            ([2 + 2j, 1 + 1j], [4 + 4j, 2 + 2j]),                # Parallel vectors
            ([1 + 1j, 2 + 2j, 3 + 3j], [4 + 4j, 5 + 5j, 6 + 6j]) # General case
        ]

        for u, v in test_cases:
            print(f"u: {u}")
            print(f"v: {v}")
            try:
                print("Cosine complex numbers:", angle_cos_complex(u, v))
            except ValueError as e:
                print("Error:", e)
            print()

    else:
        # Test cases
        test_cases = [
            ([1, 0], [1, 0]),      # Parallel vectors
            ([1, 0], [0, 1]),      # Orthogonal vectors
            ([-1, 1], [1, -1]),    # Opposite direction vectors
            ([2, 1], [4, 2]),      # Parallel vectors
            ([1, 2, 3], [4, 5, 6]) # General case
        ]

        for u, v in test_cases:
            print(f"u: {u}")
            print(f"v: {v}")
            try:
                print("Cosine:", angle_cos(u, v))
            except ValueError as e:
                print("Error:", e)
            print()
