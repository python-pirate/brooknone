from demo import *
import random

def test_max_min():
    arr = []
    
    i = 0
    while i < 10:
        arr.append(random.randint(10, 99))
        i += 1

    bmax = max_min(arr)
    for x in arr:
        assert(bmax >= x)
