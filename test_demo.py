from demo import *
import random

def test_max_min():
    for _ in range(10000):
        i = 0
        arr = []
        
        while i < 10:
            arr.append(random.randint(10, 99))
            i += 1

        bmax = max_min(arr)
        for x in arr:
            assert(bmax >= x)
