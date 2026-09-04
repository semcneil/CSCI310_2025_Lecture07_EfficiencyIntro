"""
EfficiencyComparison.py
====================================
This script does some of the efficiency comparisons shown in 
https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html

| Author: Seth McNeill
| Date: 2025 September 05
"""

import time  # for timing how long each algorithm takes
import matplotlib.pyplot as plt  # to plot results (uv pip install matplotlib)
import psutil

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
    start_cpu = time.process_time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end_cpu = time.process_time()

    end = time.time()

    return theSum,end-start, end_cpu-start_cpu


def sumOfN3(n):
    """
    Sums the numbers from 1 to N using formula rather than brute force summing

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
    theSum = (n*(n+1))/2 
    end = time.time()
    return theSum,end-start



if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library
    """
    start_time = time.time()
    nTest = 5
    nVals = [10000, 100000, 1000000, 5000000, 10000000, 100000000]
    v2Results = {'n':[], 'tavg':[]}
    v3Results = {'n':[], 'tavg':[]}
    for n in nVals:
        print(f'Times for {n}')
        tSum = 0.0
        for i in range(nTest):
            (val, t, t_cpu) = sumOfN2(n)
            print(f"Sum is {val} required {t:10.7} seconds (wall), and {t_cpu:10.7} cpu")
            tSum += t
        tavg = tSum/nTest
        print(f'Avg: {tavg}')
        print('-'*20)
        v2Results['n'].append(n)
        v2Results['tavg'].append(tavg)
    print(v2Results)

    for n in nVals:
        print(f'Times for {n} V3')
        tSum = 0.0
        for i in range(nTest):
            (val, t) = sumOfN3(n)
            print(f"Sum is {val} required {t:10.7} seconds")
            tSum += t
        tavg = tSum/nTest
        print(f'Avg: {tavg}')
        print('-'*20)
        v3Results['n'].append(n)
        v3Results['tavg'].append(tavg)
    print(v3Results)

    end_time = time.time()
    print(f"time.time time = {end_time - start_time}")
    p = psutil.Process()
    cpu_times = p.cpu_times()
    print(f"User CPU time: {cpu_times.user} seconds")
    print(f"System (Kernel) CPU time: {cpu_times.system} seconds")
    
    ## The following should work on Linux and Windows but not MacOS
    # assigned_cores = p.cpu_affinity()
    # print(f"Assigned CPU Cores: {assigned_cores}")
    # print(f"Total Assigned Count: {len(assigned_cores)}")


    # plot the results
    fig, ax = plt.subplots(figsize=(11,8.5))
    plt.rcParams['font.size'] = '18'
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(18)
    ax.plot(v2Results['n'], v2Results['tavg'], '-bo', label='V2')
    ax.plot(v3Results['n'], v3Results['tavg'], '-ro', label='V3')
    plt.xlabel('Number of Sums', fontsize=20)
    plt.ylabel(f'Avg time over {nTest} runs', fontsize=20)
    plt.grid()
    plt.title('Sum of 1 to N Algorithm Times', fontsize=24)
    plt.legend()
    plt.show()