import random

def max_min(ar):
    i = 0
    m = 0
    while i < len(ar):
        if ar[m] < ar[i]:
            m = i
        i += 1

    return ar[m]
