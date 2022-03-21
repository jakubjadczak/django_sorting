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
    counter = 0
    knuth = 1
    n = len(T)
    while knuth < n:
        knuth = knuth * 3 + 1
    knuth //= 3

    while knuth > 0:
        for i in range(knuth, n):
            j = i
            mem = T[i]
            counter += 1
            while j >= knuth:
                if T[j-knuth] < mem:
                    counter += 1
                    T[j] = T[j - knuth]
                    j -= knuth
                else:
                    break
            T[j] = mem
        knuth //= 3

    return T


