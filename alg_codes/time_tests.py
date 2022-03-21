from shell_sort import shell_sort
from numbers_gen import DataGenerator
import matplotlib.pyplot as plt


def time_test(func, n):
    avg_time = 0
    for _ in range(10):
        dg = DataGenerator()
        T = dg.random_number(n)
        R, delta = func(T)
        avg_time += delta

    return avg_time / 10


k = 100
ns = []
times = []
for _ in range(7):
    time = time_test(shell_sort, k)
    ns.append(k)
    times.append(time)
    k *= 3

print(times)
print(ns)

fig, ax = plt.subplots()
ax.plot(times, ns, 'ro')

ax.set(xlabel='czas(s)', ylabel='liczba liczb', title='Czas sortowania')
ax.grid()

fig.savefig('test.png')
plt.show()