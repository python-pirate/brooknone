from demo import *
import random

def test_max_min():
    arr = []
    for a in arr:
        arr.append(random.randint(10, 99))

    bmax = max_min(arr)
    for x in arr:
        assert(bmax >= x)
        