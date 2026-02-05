import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mpp = Counter(x)
    maxi = 0
    maxv = 0
    for k,v in mpp.items():
        if mpp[k] > maxv:
            maxi = k
            maxv = v 

    t = (np.mean(x),np.median(x),maxi)
    return t