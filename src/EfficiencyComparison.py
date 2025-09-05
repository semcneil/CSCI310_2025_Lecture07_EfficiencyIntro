"""
EfficiencyComparison.py
====================================
This script does some of the efficiency comparisons shown in 
https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html

| Author: Seth McNeill
| Date: 2025 September 05
"""

import time

def sumOfN2(n):
    """
    Sums the numbers from 1 to N

    Parameters
    ----------
    n : int
        The maximum number to sum to

    Returns
    -------
    tuple
        A two part tuple, the first part is the sum, the second is execution time
    """
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end = time.time()

    return theSum,end-start


if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    for i in range(5):
        (val, t) = sumOfN2(10000)
        print(f"Sum is {val} required {t:10.7} seconds")