"""
anagrams.py
====================================
This script does the anagram comparisons from
https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html#an-anagram-detection-example

| Author: Seth McNeill
| Date: 2026 September 04
"""

import time
import random
import string
import tracemalloc

def generate_random_string(n):
    # Choose characters to include (e.g., ascii letters and digits)
    # characters = string.ascii_letters + string.digits
    
    # Randomly select n characters and join them into a string
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def anagramSolution1(s1,s2):
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

if __name__ == "__main__":
    N = 10000
    # s1 = 'a'*N
    # s2 = 'a'*N

    s1 = generate_random_string(N)
    s2 = generate_random_string(N)

    t1s = time.time()
    tracemalloc.start()
    anagramSolution1(s1, s2)
    t1e = time.time()
    print(f"Algorithm 1 took : {t1e - t1s}")
    # Get statistics: (current_bytes, peak_bytes)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage:    {peak / 10**6:.2f} MB")

    # Stop tracking and clean up
    tracemalloc.stop()

    t2s = time.time()
    tracemalloc.start()
    anagramSolution2(s1, s2)
    t2e = time.time()
    print(f"Algorithm 2 took : {t2e - t2s}")
    # Get statistics: (current_bytes, peak_bytes)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage:    {peak / 10**6:.2f} MB")

    # Stop tracking and clean up
    tracemalloc.stop()


    t4s = time.time()
    tracemalloc.start()
    anagramSolution4(s1, s2)
    t4e = time.time()
    print(f"Algorithm 4 took : {t4e - t4s}")
    # Get statistics: (current_bytes, peak_bytes)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage:    {peak / 10**6:.2f} MB")

    # Stop tracking and clean up
    tracemalloc.stop()

