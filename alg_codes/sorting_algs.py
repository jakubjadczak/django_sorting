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

    return T, knuths, comp, swap


@delta_time
def quick_sort(T, left, right, comp=0, swap=0, pivots=None):
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
        quick_sort(T, left, q, comp, swap, pivots)
    if right > p:
        quick_sort(T, p, right, comp, swap, pivots)

    return T, pivots, comp, swap


def heap2(list, n, i):
    p = 0
    z = 0
    por = 0
    zam = 0
    dad = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and list[i] > list[l]:
        por += 1
        dad = l

    if r < n and list[dad] > list[r]:
        por += 1
        dad = r

    if dad != i:
        zam += 1
        list[i], list[dad] = list[dad], list[i]
        list,p,z = heap2(list, n, dad)
        por += p
        zam += z
    return list,por,zam


@delta_time
def heap_sort(list):
    por = 0
    zam = 0
    p = 0
    z = 0
    n = len(list)

    for i in range(n//2, -1, -1):
        list,p,z = heap2(list, n, i)
        por += p
        zam += z

    for i in range(n-1, 0, -1):
        zam += 1
        list[i], list[0] = list[0], list[i]
        list,p,z = heap2(list, i, 0)
        por += p
        zam += z

    return list,por,zam


@delta_time
def insertion_sort(list):
    comp = 0
    zamiana = 0
    for i in range(1, len(list)):
        remember = list[i]
        j = i - 1
        comp+=1
        while j >= 0 and remember > list[j]:
            comp+=1
            zamiana+=1
            list[j + 1] = list[j]
            j = j - 1
        list[j+1] = remember
    return list, comp, zamiana


@delta_time
def merge_sort(list,porownania=0,scalania=0):
    if len(list) > 1:
        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]
        merge_sort(left,porownania,scalania)
        merge_sort(right,porownania,scalania)
        i = 0
        j = 0
        k = 0
        porownania +=1
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
            porownania +=1
            scalania += 1
        porownania +=1
        while i < len(left):
            porownania += 1
            list[k] = left[i]
            i += 1
            k += 1

        porownania += 1
        while j < len(right):
            porownania += 1
            list[k] = right[j]
            j += 1
            k += 1

    return list,porownania,scalania

