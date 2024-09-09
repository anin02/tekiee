from django.test import TestCase, Client
from .models import Product
from django.utils import timezone

class TekieeTest(TestCase):
    def setUp(self):
        # Buat beberapa produk contoh untuk digunakan dalam tes
        Product.objects.create(
            name="Cool Sunglasses",
            price=150,
            description="Stylish sunglasses with UV protection.",
            frame_material="Plastic",
            lens_type="UV",
            color="Black",
            size="Medium",
            stock=20,
            brand="SunGlare"
        )
        Product.objects.create(
            name="Classic Reading Glasses",
            price=80,
            description="Comfortable reading glasses for daily use.",
            frame_material="Metal",
            lens_type="Anti-glare",
            color="Silver",
            size="Small",
            stock=50,
            brand="ReadEasy"
        )

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)

    # def test_product_list_page(self):
    #     response = Client().get('/shop/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'shop/product_list.html')

    def test_product_strong_stock(self):
        product = Product.objects.get(name="Cool Sunglasses")
        self.assertTrue(product.stock > 10)  # Assuming that if stock is greater than 10, it's considered "strong"
    
    def test_product_strong_stock_low(self):
        product = Product.objects.get(name="Classic Reading Glasses")
        self.assertTrue(product.stock > 10)  # Assuming that if stock is greater than 10, it's considered "strong"
