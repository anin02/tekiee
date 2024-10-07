from django.shortcuts import render, redirect  # Tambahkan import redirect di baris ini
from main.forms import ProductForm  # Import ProductForm untuk form produk
from main.models import Product  # Import model Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Fungsi untuk membuat produk baru
def create_product_entry(request):
    # Inisialisasi form dengan data POST atau kosong
    form = ProductForm(request.POST or None)

    # Jika form valid dan metode request adalah POST
    if form.is_valid() and request.method == "POST":
        # Simpan data produk ke database
        product_entry = form.save(commit=False)  # Commit False untuk mengatur user
        product_entry.user = request.user  # Menetapkan user yang membuat produk
        product_entry.save()  # Simpan produk
        # Redirect ke halaman utama setelah produk berhasil disimpan
        return redirect('main:show_main')

    # Buat konteks untuk template dengan form
    context = {'form': form}
    # Render halaman create_product_entry.html dengan form
    return render(request, "create_product_entry.html", context)

@login_required(login_url='/login')
def show_main(request):
    
    # Membuat konteks untuk template
    context = {
        'name': request.user.username,  # Nama pemilik
        'class': 'PBP B',  # Kelas
        'npm': '2306218111',  # NPM
        'last_login': request.COOKIES['last_login'],
    }

    # Render template 'main.html' dengan konteks yang sudah dibuat
    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Dapatkan produk berdasarkan id
    product = Product.objects.get(pk=id, user=request.user)  # Hanya produk milik user yang sedang login

    # Inisialisasi form dengan data POST atau produk yang sudah ada
    form = ProductForm(request.POST or None, instance=product)

    # Jika form valid dan metode request adalah POST
    if form.is_valid() and request.method == "POST":
        # Simpan perubahan produk
        form.save()
        # Redirect ke halaman utama setelah berhasil menyimpan perubahan
        return HttpResponseRedirect(reverse('main:show_main'))

    # Buat konteks untuk template dengan form
    context = {'form': form}
    # Render halaman edit_product.html dengan form
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Ambil produk berdasarkan id
    product = Product.objects.get(pk=id)
    # Hapus produk
    product.delete()
    # Kembali ke halaman utama
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = Product(
        name=name, price=price,
        description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
