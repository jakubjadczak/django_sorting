import time

def partition(T: list, left, right):
    pivot = T[right]
    i = left - 1
    for j in range(left, right):
        if T[j] >= pivot:
            i = i + 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[right] = T[right], T[i + 1]

    return i + 1


def quick_sort(T, left, right):
    start = time.time()
    if left < right:
        part = partition(T, left, right)
        quick_sort(T, left, part - 1)
        quick_sort(T, part + 1, right)
    stop = time.time()
    return T, stop-start

