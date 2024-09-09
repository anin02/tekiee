from django.shortcuts import render
from .models import Product  # Import model Product

def show_main(request):
    # Ambil semua produk dari database
    products = Product.objects.all()

    # Buat konteks dengan data produk
    context = {
        'products': products
    }

    # Render template dengan konteks
    return render(request, "main.html", context)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
