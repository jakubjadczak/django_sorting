from django.shortcuts import render, redirect
from django.views import View
from alg_codes.sorting_algs import shell_sort, quick_sort, insertion_sort, merge_sort, heap_sort
from django.contrib import messages
from .utils import chart_gen, sort, sort_custom_seq

global time, sorted_list, swap, comp, operations, pivots, scal, knuth, operation


def choose_alg(request):
    return render(
        request=request,
        template_name='algorithms/choose_alg.html'
    )


class HeapSort(View):

    @staticmethod
    def post(request, *args, **kwargs):
        global sorted_list, swap, comp, time
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            sorted_list, comp, swap, time, temp = sort_custom_seq(seq, heap_sort)
            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
            }
        else:
            if length and select_seq:
                length = int(length)
                if length > 100_000_000:
                    messages.add_message(request, messages.ERROR, 'Proszę podać liczbę max do miliona')
                else:
                    time, comp, swap = sort(select_seq, length, heap_sort)
                    sorted_list = '-----'
            else:
                messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
            }

        return render(
            request=request,
            template_name='algorithms/sort_for_heap.html',
            context=context
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
        global time, sorted_list, swap, comp
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            sorted_list, comp, swap, time, temp = sort_custom_seq(seq, insertion_sort)

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
            }
        else:
            if length and select_seq:
                length = int(length)
                if length > 100_000_000:
                    messages.add_message(request, messages.ERROR, 'Proszę podać liczbę max do miliona')
                else:
                    time, comp, swap = sort(select_seq, length, insertion_sort)
                    sorted_list = '-----'
            else:
                messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
            }

        return render(
            request=request,
            template_name='algorithms/sort_for_inst.html',
            context=context
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
        global sorted_list, scal, comp, time
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            sorted_list, comp, scal, time, temp = sort_custom_seq(seq, merge_sort)

            context = {
                'time': time,
                'comp': comp,
                'scal': scal,
                'sorted_list': sorted_list,
                'unsorted_list': temp,
            }
        else:
            if length and select_seq:
                length = int(length)
                if length > 100_000_000:
                    messages.add_message(request, messages.ERROR, 'Proszę podać liczbę max do miliona')
                else:
                    time, comp, scal = sort(select_seq, length, heap_sort)
                    sorted_list = '-----'
            else:
                messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'comp': comp,
                'scal': scal,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
            }

        return render(
            request=request,
            template_name='algorithms/sort_for_merge.html',
            context=context
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
        global time, sorted_list, operations, pivots, comp, swap
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            sorted_list, comp, swap, pivots, time, temp = sort_custom_seq(seq, quick_sort)

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
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
                    time, comp, swap = sort(select_seq, length, quick_sort)
            else:
                messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'pivot': []
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
        global time, sorted_list, knuth, operation, comp, swap
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        if seq:
            sorted_list, comp, swap, knuth, time, temp = sort_custom_seq(seq, quick_sort)
            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
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
                    time, comp, swap = sort(select_seq, length, heap_sort)
                    sorted_list = '-----'

            else:
                messages.add_message(request, messages.ERROR, 'Prosze podać rodzaj ciągu')

            context = {
                'time': time,
                'comp': comp,
                'swap': swap,
                'sorted_list': sorted_list,
                'unsorted_list': sorted_list,
                'knuth': []
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


class ShellSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        if k >= 10:
            chart_title = chart_gen(k, m, n, shell_sort)
            request.session['chart'] = f'Shell_Sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/shell_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/shell_test.html',
        )


class MergeSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        if k >= 10:
            chart_title = chart_gen(k, m, n, merge_sort)
            request.session['chart'] = f'Merge_Sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/shell_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/shell_test.html',
        )


class QuickSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        if k >= 10:
            chart_title = chart_gen(k, m, n, quick_sort)
            request.session['chart'] = f'Quick_Sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/shell_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/shell_test.html',
        )


class HeapSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        if k >= 10:
            chart_title = chart_gen(k, m, n, heap_sort)
            request.session['chart'] = f'Heap_Sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/shell_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/shell_test.html',
        )


class InsertionSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        k = request.POST.get('k')
        m = request.POST.get('m')
        i = request.POST.get('i')

        k = int(k)
        m = int(m)
        n = int(i)

        if k >= 10:
            chart_title = chart_gen(k, m, n, insertion_sort)
            request.session['chart'] = f'Insertion_Sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/shell_test.html'
            )

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
