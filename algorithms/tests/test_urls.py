from django.test import SimpleTestCase
from django.urls import reverse, resolve
from algorithms.views import (
                    choose_alg, HeapSort, InsertionSort,
                    ShellSort, QuickSort, MergeSort,
                    ShellSortTest, DisplayChart, HeapSortTest,
                    MergeSortTest, InsertionSortTest, QuickSortTest,
                    )


class TestUrls(SimpleTestCase):

    def test_choose(self):
        url = reverse('algor:choose')
        self.assertEqual(resolve(url).func, choose_alg)

    def test_heap_sort(self):
        url = reverse('algor:heap')
        self.assertEqual(resolve(url).func.view_class, HeapSort)

    def test_insertion_sort(self):
        url = reverse('algor:insertion')
        self.assertEqual(resolve(url).func.view_class, InsertionSort)

    def test_shell_sort(self):
        url = reverse('algor:shell')
        self.assertEqual(resolve(url).func.view_class, ShellSort)

    def test_quick_sort(self):
        url = reverse('algor:quick')
        self.assertEqual(resolve(url).func.view_class, QuickSort)

    def test_merge_sort(self):
        url = reverse('algor:merge')
        self.assertEqual(resolve(url).func.view_class, MergeSort)

    def test_shell(self):
        url = reverse('algor:shell_test')
        self.assertEqual(resolve(url).func.view_class, ShellSortTest)

    def test_heap(self):
        url = reverse('algor:heap_test')
        self.assertEqual(resolve(url).func.view_class, HeapSortTest)

    def test_merge(self):
        url = reverse('algor:merge_test')
        self.assertEqual(resolve(url).func.view_class, MergeSortTest)

    def test_insertion(self):
        url = reverse('algor:insertion_test')
        self.assertEqual(resolve(url).func.view_class, InsertionSortTest)

    def test_quick(self):
        url = reverse('algor:quick_test')
        self.assertEqual(resolve(url).func.view_class, QuickSortTest)

    def test_chart(self):
        url = reverse('algor:display_chart')
        self.assertEqual(resolve(url).func.view_class, DisplayChart)
