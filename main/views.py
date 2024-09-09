from django.shortcuts import render
#from .models import Product  # Import model Product

def show_main(request):
    # Ambil semua produk dari database
    #products = Product.objects.all()

    # Buat konteks dengan data produk
    context = {
        "name": "Kacamata 1",
        "price": 100,
        "description": "Polarized",
        "image_url": "https://www.charleskeith.co.id/dw/image/v2/BCWJ_PRD/on/demandware.static/-/Sites-id-products/default/dw246086b7/images/hi-res/2024-L3-CK3-71280563-34-1.jpg?sw=756&sh=1008",
        "nama" : "Anindhyaputri Paramitha",
        "kelas" : "PBP B",
        "NPM" : "2306218111"
    }

    # Render template dengan konteks
    return render(request, "main.html", context)
