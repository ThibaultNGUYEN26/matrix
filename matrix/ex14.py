import numpy as np
import subprocess
import time

def projection(fov, ratio, near, far):
    """
    Creates a 4x4 perspective projection matrix.
    """
    # Calculate perspective projection elements
    f = 1 / np.tan(fov / 2)  # Cotangent of half FOV
    depth = far - near

    # Construct the projection matrix in column-major order
    proj = np.zeros((4, 4))
    proj[0, 0] = f / ratio
    proj[1, 1] = f
    proj[2, 2] = -(far + near) / depth
    proj[2, 3] = -2 * far * near / depth
    proj[3, 2] = -1
    proj[3, 3] = 0

    return proj


if __name__ == "__main__":
    # Example parameters for the projection matrix
    fov = np.radians(60)
    ratio = 1.0
    near = 1.0
    far = 10.0

    # Generate the projection matrix
    proj_matrix = projection(fov, ratio, near, far)

    # Save the projection matrix to a file called "proj"
    np.savetxt('proj', proj_matrix, fmt='%.5f', delimiter=', ')
    print("Projection matrix saved to 'proj'.")

    # Run your 3D display software (e.g., ./display)
    print("Run your display program to visualize the projection.")

    time.sleep(1)

    # Run the `display` script
    subprocess.run(["./display"])
