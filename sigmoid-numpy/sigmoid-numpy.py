import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x,dtype=float)
    exp = np.exp(-x)
    sigm = 1/(1+exp)
    return sigm
    pass