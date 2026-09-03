"""
inClass20250905.py
====================================
This is from class on 2025 September 05

This script does some of the efficiency comparisons shown in 
https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html

| Author: Seth McNeill
| Date: 2025 September 05
"""

import time  # for timing operations


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
    start_time = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    end_time = time.time()

    return theSum,end_time-start_time

if __name__ == "__main__":
    for n in [10000, 100000, 1000000, 10000000]:
        print(f'{n} : {sumOfN2(n)[1]}')
