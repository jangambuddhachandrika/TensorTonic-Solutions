import numpy as np

def relu(x) -> np.ndarray:
    """Return ReLU applied elementwise to x."""
    x = np.asarray(x, dtype=float)
    return np.asarray(np.maximum(0.0, x))
    # Write code here
    pass