from django.shortcuts import render, redirect
from django.views import View
from alg_codes.numbers_gen import DataGenerator
from alg_codes.sorting_algs import shell_sort, quick_sort
import copy
from django.contrib import messages
import matplotlib.pyplot as plt
from .utils import get_random_text, chart_gen
from sorl.thumbnail import get_thumbnail


def choose_alg(request):
    return render(
        request=request,
        template_name='algorithms/choose_alg.html'
    )


class HeapSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        return render(
            request=request,
            template_name='algorithms/sort_for_heap.html',
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_heap.html',
        )


class InsertionSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        return render(
            request=request,
            template_name='algorithms/sort_for_inst.html',
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_inst.html',
        )


class MergeSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        return render(
            request=request,
            template_name='algorithms/sort_for_merge.html',
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_merge.html',
        )


class QuickSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        global time, sorted_list, operations, pivots
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            seq = seq.split()
            seq = [int(i) for i in seq]
            temp = copy.deepcopy(seq)
            result = quick_sort(seq, 0, len(seq) - 1)
            sorted_list = result[0][0]
            pivots = result[0][1]
            operations = result[0][2]
            time = result[1]
            context = {
                'time': time,
                'operation': operations,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
                'pivot': pivots
            }
        else:
            if length and select_seq:
                length = int(length)
                if length > 100_000_000:
                    messages.add_message(request, messages.ERROR, 'Proszę podać liczbę max do miliona')
                else:
                    dg = DataGenerator()
                    if select_seq == 'A':
                        T = dg.a_shape(length)
                        result = quick_sort(T, 0, len(T) - 1)
                        time = result[1]
                        pivots = result[0][1]
                        operations = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'V':
                        T = dg.v_shape(length)
                        result = quick_sort(T, 0, len(T) - 1)
                        time = result[1]
                        pivots = result[0][1]
                        operations = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'increase':
                        T = dg.increase(length)
                        result = quick_sort(T, 0, len(T) - 1)
                        time = result[1]
                        pivots = result[0][1]
                        operations = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'decrease':
                        T = dg.decrease(length)
                        result = quick_sort(T, 0, len(T) - 1)
                        time = result[1]
                        pivots = result[0][1]
                        operations = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'random':
                        T = dg.random_number(length)
                        result = quick_sort(T, 0, len(T) - 1)
                        time = result[1]
                        pivots = result[0][1]
                        operations = result[0][2]
                        sorted_list = '-----'

                    else:
                        messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'operation': operations,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'pivot': pivots
            }

        return render(
            request=request,
            template_name='algorithms/sort_for_quick.html',
            context=context
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_quick.html',
        )


class ShellSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        global time, sorted_list, knuth, operation
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            seq = seq.split()
            seq = [int(i) for i in seq]
            temp = copy.deepcopy(seq)
            result = shell_sort(seq)
            sorted_list = result[0][0]
            knuth = result[0][1]
            operation = result[0][2]
            time = result[1]
            context = {
                'time': time,
                'operation': operation,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
                'knuth': knuth
            }
        else:
            if length and select_seq:
                length = int(length)
                if length > 100_000_000:
                    messages.add_message(request, messages.ERROR, 'Proszę podać liczbę max do miliona')
                else:
                    dg = DataGenerator()
                    if select_seq == 'A':
                        T = dg.a_shape(length)
                        result = shell_sort(T)
                        time = result[1]
                        knuth = result[0][1]
                        operation = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'V':
                        T = dg.v_shape(length)
                        result = shell_sort(T)
                        time = result[1]
                        knuth = result[0][1]
                        operation = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'increase':
                        T = dg.increase(length)
                        result = shell_sort(T)
                        time = result[1]
                        knuth = result[0][1]
                        operation = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'decrease':
                        T = dg.decrease(length)
                        result = shell_sort(T)
                        time = result[1]
                        knuth = result[0][1]
                        operation = result[0][2]
                        sorted_list = '-----'

                    elif select_seq == 'random':
                        T = dg.random_number(length)
                        result = shell_sort(T)
                        time = result[1]
                        knuth = result[0][1]
                        operation = result[0][2]
                        sorted_list = '-----'

                    else:
                        messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')
            context = {
                'time': time,
                'operation': operation,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'knuth': knuth
            }

        return render(
            request=request,
            template_name='algorithms/sort_for_shell.html',
            context=context
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_shell.html',
        )


class ComparisonTest(View):
    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        shell_times = []
        quick_times = []
        seq_length = []
        dg = DataGenerator()

        for _ in range(n):
            avg_time_shell = 0
            avg_time_quick = 0

            for _ in range(2):
                T = dg.a_shape(k)
                result_shell = shell_sort(T)
                result_quick = quick_sort(T, 0, len(T) - 1)
                avg_time_shell += result_shell[1]
                avg_time_quick += result_quick[1]

            for _ in range(2):
                T = dg.v_shape(k)
                result_shell = shell_sort(T)
                result_quick = quick_sort(T, 0, len(T) - 1)
                avg_time_shell += result_shell[1]
                avg_time_quick += result_quick[1]

            for _ in range(2):
                T = dg.increase(k)
                result_shell = shell_sort(T)
                result_quick = quick_sort(T, 0, len(T) - 1)
                avg_time_shell += result_shell[1]
                avg_time_quick += result_quick[1]

            for _ in range(2):
                T = dg.decrease(k)
                result_shell = shell_sort(T)
                result_quick = quick_sort(T, 0, len(T) - 1)
                avg_time_shell += result_shell[1]
                avg_time_quick += result_quick[1]

            for _ in range(2):
                T = dg.random_number(k)
                result_shell = shell_sort(T)
                result_quick = quick_sort(T, 0, len(T) - 1)
                avg_time_shell += result_shell[1]
                avg_time_quick += result_quick[1]

            seq_length.append(k)
            shell_times.append(avg_time_shell / 10)
            quick_times.append(avg_time_quick / 10)
            k *= m

        chart_title = get_random_text()

        fig_shell, ax_shell = plt.subplots()
        ax_shell.plot(shell_times, seq_length, 'ro')
        ax_shell.set(xlabel='Czas(s)', ylabel='Wielkość ciągu', title='Czas sortowania - Shell Sort')
        ax_shell.grid()
        fig_shell.savefig(f'media/Shell_Sort_{chart_title}.png')

        fig_quick, ax_quick = plt.subplots()
        ax_quick.plot(quick_times, seq_length, 'ro')
        ax_quick.set(xlabel='Czas(s)', ylabel='Wielkość ciągu', title='Czas sortowania - Shell Sort')
        ax_quick.grid()
        fig_quick.savefig(f'media/Quick_Sort_{chart_title}.png')
        # image = Image.objects.create(title)
        # image.save()
        # plt.show()

        request.session['shell_chart'] = f'Shell_Sort_{chart_title}'
        request.session['quick_chart'] = f'QuickSort_{chart_title}'

        return redirect('algor:display_chart')

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/comparison_test.html',
        )


class ShellSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        chart_title = chart_gen(k,m,n,shell_sort)

        request.session['chart'] = f'Shell_Sort_{chart_title}.png'

        return redirect('algor:display_chart')

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/shell_test.html',
        )


class DisplayChart(View):

    @staticmethod
    def post(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/display_chart.html'
        )

    @staticmethod
    def get(request, *args, **kwargs):
        title = request.session['chart']
        return render(
            request=request,
            template_name='algorithms/display_chart.html',
            context={'name': title}
        )


class DisplayCharts(View):

    @staticmethod
    def post(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/display_chart.html'
        )

    @staticmethod
    def get(request, *args, **kwargs):
        titles = [request.session['shell_chart'], request.session['quick_chart']]

        return render(
            request=request,
            template_name='algorithms/display_chart.html',
            context={'titles': titles}
        )

