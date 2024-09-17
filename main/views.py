from django.shortcuts import render, redirect  # Tambahkan import redirect di baris ini
from main.forms import ProductForm  # Import ProductForm untuk form produk
from main.models import Product  # Import model Product
from django.http import HttpResponse
from django.core import serializers

# Fungsi untuk membuat produk baru
def create_product_entry(request):
    # Inisialisasi form dengan data POST atau kosong
    form = ProductForm(request.POST or None)

    # Jika form valid dan metode request adalah POST
    if form.is_valid() and request.method == "POST":
        # Simpan data produk ke database
        form.save()
        # Redirect ke halaman utama setelah produk berhasil disimpan
        return redirect('main:show_main')

    # Buat konteks untuk template dengan form
    context = {'form': form}
    # Render halaman create_product_entry.html dengan form
    return render(request, "create_product_entry.html", context)

def show_main(request):
    # Mengambil semua produk dari database
    product_entries = Product.objects.all()

    # Membuat konteks untuk template
    context = {
        'name': 'Anindhyaputri Paramitha',  # Nama pemilik
        'class': 'PBP B',  # Kelas
        'npm': '2306218111',  # NPM
        'product_entries': product_entries  # Semua produk yang diambil dari database
    }

    # Render template 'main.html' dengan konteks yang sudah dibuat
    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
