from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_main_page(self):
        response = self.client.get(reverse('algor:choose'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/choose_alg.html')

    def test_display_chart(self):
        response = self.client.get(reverse('algor:display_chart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/display_chart.html')

    def test_heap(self):
        response = self.client.get(reverse('algor:heap_test'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/heap_test.html')

    def test_insertion(self):
        response = self.client.get(reverse('algor:insertion_test'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/insertion_test.html')

    def test_merge(self):
        response = self.client.get(reverse('algor:merge_test'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/merge_test.html')

    def test_quick(self):
        response = self.client.get(reverse('algor:quick_test'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/quick_test.html')

    def test_shell(self):
        response = self.client.get(reverse('algor:shell_test'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/shell_test.html')

    def test_sort_heap(self):
        response = self.client.get(reverse('algor:heap'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/sort_for_heap.html')

    def test_sort_insertion(self):
        response = self.client.get(reverse('algor:insertion'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/sort_for_inst.html')

    def test_sort_merge(self):
        response = self.client.get(reverse('algor:merge'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/sort_for_merge.html')

    def test_sort_quick(self):
        response = self.client.get(reverse('algor:quick'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/sort_for_quick.html')

    def test_sort_shell(self):
        response = self.client.get(reverse('algor:shell'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'algorithms/sort_for_shell.html')
