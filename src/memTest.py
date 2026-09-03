"""
memTest.py
====================================
This script tests ways to measure memory usage of algorithms.

| Author: Seth McNeill
| Date: 2026 September 03
"""

import time  # for timing how long each algorithm takes
import matplotlib.pyplot as plt  # to plot results (uv pip install matplotlib)
import tracemalloc  # tracks memory usage

if __name__ == '__main__':
    """Runs if file called as script as opposed to being imported as a library

    These examples originally came from standard Google search AI
    """


    # Start tracking memory allocations
    tracemalloc.start()

    # --- Run your code here ---
    data = [x for x in range(100000)]  # creates a large list
    del data  # deletes a variable to release the memory
    # --------------------------

    # Get statistics: (current_bytes, peak_bytes)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage:    {peak / 10**6:.2f} MB")

    # Stop tracking and clean up
    tracemalloc.stop()

    print('\n' + '='*40 + '\n') 

#######################
    # second method attempt
    tracemalloc.start()
    leaky_global_list = []
    snapshot_before = tracemalloc.take_snapshot()

    for i in range(5000):
        leaky_global_list.append(dict(id=i, val="leak"))

    snapshot_after = tracemalloc.take_snapshot()
    top_diffs = snapshot_after.compare_to(snapshot_before, 'lineno')

    print("[ Top Memory Increases ]")
    for diff in top_diffs[:3]:
        print(diff)
    tracemalloc.stop()

    print('\n' + '='*40 + '\n') 

#######################
    # third method attempt
    tracemalloc.start(3)
    big_strings = [str(i) * 50 for i in range(50000)]
    big_strings2 = ['abcdefg' for i in range(50000)]
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 3 Allocations ]")
    for index, stat in enumerate(top_stats[:3], 1):
        print(f"#{index}: {stat}")