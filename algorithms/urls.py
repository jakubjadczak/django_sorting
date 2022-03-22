from django.urls import path
from .views import (choose_alg, HeapSort, InsertionSort,
                    ShellSort, QuickSort, MergeSort,
                    ShellSortTest, DisplayChart
                    )

app_name = 'algor'

urlpatterns = [
    path('', choose_alg, name='choose'),
    path('heap-sort/', HeapSort.as_view(), name='heap'),
    path('insertion-sort/', InsertionSort.as_view(), name='insertion'),
    path('shell-sort/', ShellSort.as_view(), name='shell'),
    path('quick-sort/', QuickSort.as_view(), name='quick'),
    path('merge-sort/', MergeSort.as_view(), name='merge'),
    path('shell-test/', ShellSortTest.as_view(), name='shell_test'),
    path('shell-chart/', DisplayChart.as_view(), name='display_chart'),
]