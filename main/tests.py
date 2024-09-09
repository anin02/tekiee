from django.test import TestCase, Client
from django.urls import reverse

class ShowMainViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('show_main')  # Pastikan nama URL sesuai dengan nama view

    def test_show_main_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_show_main_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'main.html')

    def test_show_main_view_context(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Kacamata 1")
        self.assertContains(response, "$100")
        self.assertContains(response, "Polarized")
        self.assertContains(response, "https://www.charleskeith.co.id/dw/image/v2/BCWJ_PRD/on/demandware.static/-/Sites-id-products/default/dw246086b7/images/hi-res/2024-L3-CK3-71280563-34-1.jpg?sw=756&sh=1008")
        self.assertContains(response, "Anindhyaputri Paramitha")
        self.assertContains(response, "PBP B")
        self.assertContains(response, "2306218111")