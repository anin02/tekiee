from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    # def test_show_main_view_product_data(self):
    #     # Mengambil data dari view
    #     response = self.client.get(self.url)
        
    #     # Memeriksa data produk dalam konteks
    #     self.assertIn('name', response.context)
    #     self.assertIn('price', response.context)
    #     self.assertIn('description', response.context)
    #     self.assertIn('image_url', response.context)
    #     self.assertIn('nama', response.context)
    #     self.assertIn('kelas', response.context)
    #     self.assertIn('NPM', response.context)

    #     # Validasi data produk
    #     self.assertEqual(response.context['name'], 'Kacamata 1')
    #     self.assertEqual(response.context['price'], 100)
    #     self.assertEqual(response.context['description'], 'Polarized')
    #     self.assertEqual(response.context['image_url'], "https://www.charleskeith.co.id/dw/image/v2/BCWJ_PRD/on/demandware.static/-/Sites-id-products/default/dw246086b7/images/hi-res/2024-L3-CK3-71280563-34-1.jpg?sw=756&sh=1008")
    #     self.assertEqual(response.context['nama'], 'Anindhyaputri Paramitha')
    #     self.assertEqual(response.context['kelas'], 'PBP B')
    #     self.assertEqual(response.context['NPM'], '2306218111')