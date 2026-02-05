import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    mean = np.sum((x - np.mean(x))**2)/(len(x)-1)
    tup = (mean,np.sqrt(mean))
    return tup