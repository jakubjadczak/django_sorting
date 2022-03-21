from django.shortcuts import render
from django.views import View
from alg_codes.shell_sort import shell_sort
from alg_codes.numbers_gen import DataGenerator
from alg_codes.quick_sort import quick_sort
import copy
from django.contrib import messages


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
        global time, sorted_list
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            seq = seq.split()
            seq = [int(i) for i in seq]
            temp = copy.deepcopy(seq)
            result = quick_sort(seq, 0, len(seq)-1)
            sorted_list = result[0]
            time = result[1]
            context = {
                'time': time,
                'operation': 0,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
                'pivot': 0
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
                        result = quick_sort(T, 0, len(T)-1)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'V':
                        T = dg.v_shape(length)
                        result = quick_sort(T, 0, len(T)-1)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'increase':
                        T = dg.increase(length)
                        result = quick_sort(T, 0, len(T)-1)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'decrease':
                        T = dg.decrease(length)
                        result = quick_sort(T, 0, len(T)-1)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'random':
                        T = dg.random_number(length)
                        result = quick_sort(T, 0, len(T)-1)
                        time = result[1]
                        sorted_list = '-----'

                    else:
                        messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'operation': 0,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'pivot': 0
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
        global time, sorted_list
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            seq = seq.split()
            seq = [int(i) for i in seq]
            temp = copy.deepcopy(seq)
            result = shell_sort(seq)
            sorted_list = result[0]
            time = result[1]
            context = {
                'time': time,
                'operation': 0,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
                'knuth': 0
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
                        sorted_list = '-----'

                    elif select_seq == 'V':
                        T = dg.v_shape(length)
                        result = shell_sort(T)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'increase':
                        T = dg.increase(length)
                        result = shell_sort(T)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'decrease':
                        T = dg.decrease(length)
                        result = shell_sort(T)
                        time = result[1]
                        sorted_list = '-----'

                    elif select_seq == 'random':
                        T = dg.random_number(length)
                        result = shell_sort(T)
                        time = result[1]
                        sorted_list = '-----'

                    else:
                        messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')
            context = {
                'time': time,
                'operation': 0,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'knuth': 0
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
