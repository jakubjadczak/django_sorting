import random
import string
from alg_codes.numbers_gen import DataGenerator
import matplotlib.pyplot as plt
import copy


def get_random_text():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(6))


def chart_gen(k, m, n, func):
    times_a = []
    times_v = []
    times_in = []
    times_dc = []
    times_ran = []
    seq_length = []
    dg = DataGenerator()

    for _ in range(n):
        avg_time = 0
        for _ in range(10):
            T = dg.a_shape(k)
            result = func(T)
            avg_time += result[1]
        times_a.append(avg_time / 10)

        for _ in range(10):
            T = dg.v_shape(k)
            result = func(T)
            avg_time += result[1]
        times_v.append(avg_time / 10)

        for _ in range(10):
            T = dg.increase(k)
            result = func(T)
            avg_time += result[1]
        times_in.append(avg_time / 10)

        for _ in range(10):
            T = dg.decrease(k)
            result = func(T)
            avg_time += result[1]
        times_dc.append(avg_time / 10)

        for _ in range(10):
            T = dg.random_number(k)
            result = func(T)
            avg_time += result[1]
        times_ran.append(avg_time / 10)

        seq_length.append(k)
        k *= m

    fig, ax = plt.subplots()

    a_shape, = ax.plot(times_a, seq_length, label='Ciągi A')
    v_shape, = ax.plot(times_v, seq_length, label='Ciągi V')
    incr, = ax.plot(times_in, seq_length, label='Ciągi rosnące')
    dcr, = ax.plot(times_dc, seq_length, label='Ciągi malejące')
    random, = ax.plot(times_ran, seq_length, label='Ciągi losowe')

    ax.set(xlabel='Czas(s)', ylabel='Wielkość ciągu', title='Czas sortowania - Shell Sort')
    ax.legend()

    chart_title = get_random_text()

    fig.savefig(f'media/Shell_Sort_{chart_title}.png')

    return chart_title


def sort(select_seq:str, length: int, func):
    time = 0
    comp = 0
    swap = 0

    dg = DataGenerator()
    if select_seq == 'A':
        T = dg.a_shape(length)
        result = func(T)
        time = result[1]
        comp = result[0][1]
        swap = result[0][2]

    elif select_seq == 'V':
        T = dg.v_shape(length)
        result = func(T)
        time = result[1]
        comp = result[0][1]
        swap = result[0][2]

    elif select_seq == 'increase':
        T = dg.increase(length)
        result = func(T)
        time = result[1]
        comp = result[0][1]
        swap = result[0][2]

    elif select_seq == 'decrease':
        T = dg.decrease(length)
        result = func(T)
        time = result[1]
        comp = result[0][1]
        swap = result[0][2]

    elif select_seq == 'random':
        T = dg.random_number(length)
        result = func(T)
        time = result[1]
        comp = result[0][1]
        swap = result[0][2]

    return time, comp, swap


def sort_custom_seq(seq, func):
    seq= seq.split()
    seq = [int(i) for i in seq]
    temp = copy.deepcopy(seq)
    result = func(seq)

    sorted_list = result[0][0]
    comp = result[0][1]
    swap = result[0][2]
    time = result[1]

    try:
        additional = result[0][3]
        return sorted_list, comp, swap, additional, time, temp
    except IndexError:
        pass

    return sorted_list, comp, swap, time, temp

