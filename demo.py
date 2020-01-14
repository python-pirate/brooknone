def select_sort(ar):
    j = len(ar)
    while j > 1:
        i = 1
        m = 0

        while i < j:
            if ar[m] < ar[i]:
                m = i
            i += 1

        if ar[m] != ar[j - 1]:
            ar[m], ar[j - 1] = ar[j - 1], ar[m]
        j -= 1
