from demo import *
import random

def test_select_sort():
    for _ in range(10000):
        i = 0
        arr = [random.randint(10, 99) for _ in range(10)]

        select_sort(arr)

        while i < len(arr) - 1:
            assert(arr[i] <= arr[i + 1])
            i += 1
