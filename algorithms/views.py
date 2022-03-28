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
        start = request.POST.get('start')
        step = request.POST.get('step')
        stop = request.POST.get('stop')

        start = int(start)
        step = int(step)
        stop = int(stop)

        if start >= 10:
            chart_title = chart_gen(start, step, stop, shell_sort, 'shell')
            request.session['chart'] = f'shell_sort_{chart_title}.png'
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
        start = request.POST.get('start')
        step = request.POST.get('step')
        stop = request.POST.get('stop')

        start = int(start)
        step = int(step)
        stop = int(stop)

        if start >= 10:
            chart_title = chart_gen(start, step, stop, merge_sort, 'merge')
            request.session['chart'] = f'merge_sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/merge_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/merge_test.html',
        )


class QuickSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        start = request.POST.get('start')
        step = request.POST.get('step')
        stop = request.POST.get('stop')

        start = int(start)
        step = int(step)
        stop = int(stop)

        if start >= 10:
            chart_title = chart_gen(start, step, stop, quick_sort, 'quick')
            request.session['chart'] = f'quick_sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/quick_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/quick_test.html',
        )


class HeapSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        start = request.POST.get('start')
        step = request.POST.get('step')
        stop = request.POST.get('stop')

        start = int(start)
        step = int(step)
        stop = int(stop)

        if start >= 10:
            chart_title = chart_gen(start, step, stop, heap_sort, 'heap')
            request.session['chart'] = f'heap_sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/heap_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/heap_test.html',
        )


class InsertionSortTest(View):

    @staticmethod
    def post(request, *args, **kwargs):
        start = request.POST.get('start')
        step = request.POST.get('step')
        stop = request.POST.get('stop')

        start = int(start)
        step = int(step)
        stop = int(stop)

        if start >= 10:
            chart_title = chart_gen(start, step, stop, insertion_sort, 'insertion')
            request.session['chart'] = f'insertion_sort_{chart_title}.png'
            return redirect('algor:display_chart')
        else:
            messages.add_message(request, messages.ERROR, 'K musi być większe lub równe 10')
            return render(
                request=request,
                template_name='algorithms/insertion_test.html'
            )

    @staticmethod
    def get(request, *args, **kwargs):

        return render(
            request=request,
            template_name='algorithms/insertion_test.html',
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
        try:
            title = request.session['chart']
        except KeyError:
            title = ''

        return render(
            request=request,
            template_name='algorithms/display_chart.html',
            context={'name': title}
        )
