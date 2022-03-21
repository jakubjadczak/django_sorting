from django.shortcuts import render
from django.views import View


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
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        return render(
            request=request,
            template_name='algorithms/sort_for_quick.html',
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
        seq = request.POST.get('seq')
        select_seq = request.POST.get('select_seq')
        length = request.POST.get('length')

        return render(
            request=request,
            template_name='algorithms/sort_for_quick.html',
        )

    @staticmethod
    def get(request, *args, **kwargs):
        return render(
            request=request,
            template_name='algorithms/sort_for_quick.html',
        )
