import time


def delta_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        delta = stop_time - start_time

        return result, delta

    return inner


@delta_time
def shell_sort(T: list):
    comp = 0
    swap = 0
    knuth = 1
    knuths = []
    n = len(T)
    while knuth < n:
        knuth = knuth * 3 + 1

    if knuth > n:
        knuth //= 3

    while knuth > 0:
        knuths.append(knuth)
        for i in range(knuth, n):
            j = i
            mem = T[i]
            comp += 1
            while j >= knuth:
                comp += 1
                if T[j-knuth] < mem:
                    swap += 1
                    T[j] = T[j - knuth]
                    j -= knuth
                else:
                    break
            T[j] = mem
        knuth //= 3

    return T, comp, swap, knuths


@delta_time
def _quick_sort(T, left, right, comp=0, swap=0, pivots=None):
    if pivots is None:
        pivots = []

    p, q = left, right
    pivot = T[right]
    pivots.append(pivot)
    while p <= q:
        comp += 1
        while T[p] > pivot:
            p += 1
        comp += 1
        while T[q] < pivot:
            q -= 1
        if p <= q:
            swap += 1
            T[p], T[q] = T[q], T[p]
            p += 1
            q -= 1
    if left < q:
        _quick_sort(T, left, q, comp, swap, pivots)
    if right > p:
        _quick_sort(T, p, right, comp, swap, pivots)

    return T, comp, swap, pivots


def quick_sort(T):
    return _quick_sort(T, 0, len(T)-1)


def heap2(list, n, i):
    comp = 0
    swap = 0
    dad = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and list[i] > list[l]:
        comp += 1
        dad = l

    if r < n and list[dad] > list[r]:
        comp += 1
        dad = r

    if dad != i:
        swap += 1
        list[i], list[dad] = list[dad], list[i]
        list, p, z = heap2(list, n, dad)
        comp += p
        swap += z
    return list, comp, swap


@delta_time
def heap_sort(list):
    comp = 0
    swap = 0
    n = len(list)

    for i in range(n//2, -1, -1):
        list, p, z = heap2(list, n, i)
        comp += p
        swap += z

    for i in range(n-1, 0, -1):
        swap += 1
        list[i], list[0] = list[0], list[i]
        list, p, z = heap2(list, i, 0)
        comp += p
        swap += z

    return list, comp, swap


@delta_time
def insertion_sort(list):
    # print('inst')
    comp = 0
    swap = 0
    for i in range(1, len(list)):
        remember = list[i]
        j = i - 1
        comp += 1
        while j >= 0 and remember > list[j]:
            comp += 1
            swap += 1
            list[j + 1] = list[j]
            j = j - 1
        list[j+1] = remember
    return list, comp, swap


@delta_time
def merge_sort(list, comp=0, scal=0):
    # print('merge')
    if len(list) > 1:
        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]
        merge_sort(left, comp, scal)
        merge_sort(right, comp, scal)
        i = 0
        j = 0
        k = 0
        comp += 1
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
            comp += 1
            scal += 1
        comp += 1
        while i < len(left):
            comp += 1
            list[k] = left[i]
            i += 1
            k += 1

        comp += 1
        while j < len(right):
            comp += 1
            list[k] = right[j]
            j += 1
            k += 1

    return list, comp, scal
