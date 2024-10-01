Nama : Anindhyaputri Paramitha

NPM : 2306218111

Kelas : PBP B

e-commerce : tekiee (menjual berbagai jenis kacamata)

http://anindhyaputri-paramitha-tekiee.pbp.cs.ui.ac.id/



### TUGAS 2

I. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Inisiasi Direktori Lokal dan GitHub
1. Buat repositori baru di GitHub dengan nama “tekiee”.
2. Buat direktori lokal bernama "tekie" untuk menyimpan proyek git.
3. Inisiasi repositori baru dengan perintah `git init`.
4. Konfigurasi nama pengguna dan email dengan perintah `git config --global user.name "Nama Anda"` dan `git config --global user.email "email@domain.com"`.
5. Lakukan autentikasi git (`git credential-manager configure` dan `git config --global credential.credentialStore keychain`)
6. Verifikasi konfigurasi dengan `git config --list`.
7. Dalam direktori lokal "tekie", buat berkas baru bernama `README.md` 
8. Tambahkan dan commit berkas tersebut dengan perintah `git add README.md` diikuti `git commit -m "Initial commit"`.
9. Buat branch utama bernama "main" dengan `git branch -M main`.
10. Hubungkan repositori lokal ke repositori GitHub menggunakan `git remote add origin <URL_REPO>`.
11. Push perubahan ke GitHub dengan `git push -u origin main`.
12. Verifikasi apakah repositori GitHub telah berhasil di-update.

### Pembuatan dan Pengelolaan Branch
1. Buat dan beralih ke branch baru dengan perintah `git checkout -b <NAMA_BRANCH>`.
2. Lakukan perubahan, tambahkan, commit, dan push ke branch baru dengan `git add`, `git commit`, dan `git push -u origin <NAMA_BRANCH>`.
3. Di GitHub, lakukan merge pull request untuk menggabungkan branch baru ke branch utama (main).

### Inisiasi Proyek Django
1. Buat virtual environment dan aktifkan (akan terbentuk subdirektori `env` setelah diaktifkan).
2. Siapkan dependencies dan buat proyek Django. Buat berkas `requirements.txt`, install dependencies, dan buat proyek Django dengan `django-admin startproject`.
3. Setelah itu, di dalam direktori lokal "tekie", akan terbentuk beberapa berkas dan subdirektori seperti `manage.py`, `requirements.txt`, dan subdirektori proyek Django dengan nama `tekie`.
4. Edit `ALLOWED_HOSTS` di berkas `settings.py` untuk menentukan siapa yang bisa mengakses aplikasi.
5. Jalankan server Django dengan perintah `python manage.py runserver` dan buka http://localhost:8000 untuk melihat halaman Django default.
6. Untuk menghentikan server, tekan `Ctrl+C` dan nonaktifkan virtual environment.

### Unggah Proyek ke GitHub
1. Buat berkas `.gitignore` dan isi dengan daftar berkas atau direktori yang tidak perlu dilacak oleh Git, seperti file sementara atau konfigurasi pribadi.
2. Lakukan `git add`, `git commit`, dan `git push` untuk mengunggah perubahan ke GitHub.

### Pembuatan Aplikasi Django dan Konfigurasi Model
1. Aktifkan virtual environment.
2. Buat aplikasi baru bernama "main" (direktori "main" akan terbentuk dengan struktur awal aplikasi Django).
3. Daftarkan aplikasi "main" ke dalam proyek dengan menambahkannya di variabel `INSTALLED_APPS` di `settings.py`.
4. Buat berkas template `main.html` di dalam direktori `templates` di aplikasi "main" dan isi sesuai kebutuhan.
5. Buka berkas `models.py` dan tambahkan model `Product` sesuai tugas, berisi atribut `name`, `price`, dan `description`.
6. Lakukan migrasi untuk menyimpan perubahan pada model (migrasi ini akan terus dilakukan setiap mengubah models).
7. Hubungkan view dengan template, buat fungsi `show_main` di `views.py` dan sertakan data yang ingin ditampilkan.
8. Tambahkan data di `views.py` karena pada tahap ini data masih boleh disimpan di views sesuai arahan asisten dosen.
9. Modifikasi template HTML sesuai preferensi.
10. Atur routing URL di `urls.py` aplikasi "main" agar fungsi `show_main` bisa diakses melalui browser.
11. Konfigurasikan routing URL proyek di `urls.py` direktori proyek, bukan yang ada di dalam direktori aplikasi main.
12. Jalankan server Django dan buka http://localhost:8000 untuk memverifikasi halaman.

### Unit Testing
1. Buka berkas `tests.py` di aplikasi "main" dan tambahkan fungsi untuk unittest.
2. Jalankan tes untuk memastikan kode berfungsi dengan benar.

### Deployment ke PWS (Pacil Web Service)
1. Akses halaman PWS, login, dan buat proyek baru.
2. Tambahkan URL deployment PWS ke dalam `ALLOWED_HOSTS` di `settings.py`.
3. Lakukan `git add`, `commit`, dan `push` untuk mengunggah perubahan ke GitHub.
4. Jalankan perintah yang disediakan di halaman proyek PWS.
5. Jika ada perubahan di masa depan, cukup jalankan `git push pws main:master` setelah melakukan `add` dan `commit`.




II. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

### Alur Request-Response Django
### Request dari Client: 
Pengguna mengirim permintaan (request) melalui browser dengan mengakses URL aplikasi web (misalnya, http://localhost:8000/main).

### urls.py: 
Django pertama kali memproses request melalui urls.py. Berkas ini berfungsi sebagai penghubung antara URL yang diakses pengguna dengan fungsi yang sesuai di views.py. Jika URL cocok dengan pola yang didefinisikan, Django akan meneruskannya ke fungsi yang terdaftar di views.py.

### views.py: 
Di dalam views.py, fungsi yang sesuai (misalnya, show_main) akan dijalankan. Fungsi ini bertanggung jawab untuk mengambil data (baik dari models.py maupun data yang dimasukkan langsung di views.py) dan kemudian mengembalikannya dalam bentuk response.

### models.py: 
Jika fungsi di views.py membutuhkan data dari database, ia akan melakukan query melalui model yang didefinisikan di models.py. Contohnya, jika aplikasi perlu menampilkan daftar produk, fungsi akan mengakses model Product untuk mengambil data yang dibutuhkan.

### HTML Template: 
Setelah data diambil (baik dari views.py maupun models.py), data tersebut akan diteruskan ke berkas HTML (misalnya, main.html). Template HTML ini mengatur bagaimana data ditampilkan kepada pengguna.

### Response: 
Django akan mengirimkan hasil dari template HTML yang sudah diisi data sebagai response ke browser. Browser kemudian menampilkan halaman web kepada pengguna.


### Bagan Request-Response Django
![alt text](IMG_0589.jpg)

### Kaitan Antara urls.py, views.py, models.py, dan HTML Template
### urls.py: 
Menghubungkan URL dengan fungsi di views.py. Setiap URL di aplikasi web diatur di sini, sehingga ketika pengguna mengakses URL tertentu, Django akan tahu fungsi mana yang harus dipanggil.

### views.py: 
Berisi logika untuk memproses request dari pengguna. Fungsi di views.py dapat mengambil data dari models.py atau langsung mengatur data yang akan ditampilkan ke pengguna. Setelah data siap, views.py akan mengirimkan data ke template HTML untuk dirender.

### models.py: 
Berfungsi untuk berinteraksi dengan database. Jika data perlu diambil atau disimpan ke database, views.py akan memanggil model yang sesuai di models.py. Data yang diambil dari models.py kemudian dikirim ke template HTML melalui views.py.

### HTML Template: 
Berkas HTML yang berfungsi untuk menampilkan data kepada pengguna. Template ini diisi dengan data yang dikirim dari views.py dan di-render untuk menghasilkan halaman web yang bisa diakses oleh pengguna di browser.




III. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah alat penting dalam pengembangan perangkat lunak yang berfungsi untuk mengelola dan melacak perubahan kode. Dengan Git, pengembang dapat menyimpan berbagai versi kode yang disebut *commit*, sehingga setiap perubahan dapat dipantau, dibandingkan, atau dikembalikan ke versi sebelumnya jika diperlukan. Git juga memudahkan kolaborasi antar anggota tim, di mana setiap orang bisa bekerja pada cabang (*branch*) terpisah tanpa mengganggu kode utama, dan hasilnya bisa digabungkan (*merge*) saat sudah siap.

Selain itu, Git juga berguna untuk menyimpan cadangan (*backup*) proyek, sehingga jika terjadi masalah pada komputer lokal, kode tetap aman di repositori GitHub atau server lainnya. Git mencatat setiap perubahan, lengkap dengan siapa yang melakukannya dan kapan, sehingga bisa memudahkan pemantauan dan memecahkan masalah jika ada bug. 

Git juga terintegrasi dengan alat otomatis seperti Continuous Integration (CI) dan Continuous Deployment (CD), yang membantu pengembang menguji dan menerapkan perubahan secara cepat. Dengan kemampuan Git untuk mendeteksi konflik ketika ada dua orang yang mengubah kode yang sama, pengembang bisa menyelesaikan masalah tersebut dengan mudah, menjaga agar proyek tetap berjalan lancar.




IV. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan utama. Pertama, Django adalah framework yang bersifat *full-stack*, artinya Django sudah menyediakan berbagai fitur penting yang dibutuhkan dalam membangun aplikasi web, seperti manajemen database, routing URL, dan autentikasi, tanpa perlu banyak pengaturan tambahan. Hal ini memudahkan pemula untuk fokus belajar konsep-konsep inti dalam pengembangan web tanpa harus memikirkan terlalu banyak alat atau library eksternal.

Selain itu, Django menggunakan bahasa Python, yang terkenal mudah dipahami karena sintaksnya yang sederhana dan jelas. Python juga sering menjadi bahasa pertama yang dipelajari oleh banyak orang yang baru mulai belajar pemrograman, sehingga menggunakan Django sebagai framework selanjutnya terasa lebih mudah. Django juga memiliki dokumentasi yang sangat lengkap, yang memudahkan pemula untuk mengikuti langkah-langkah pembangunan aplikasi dari awal hingga akhir.

Terakhir, Django mendorong praktik pengembangan yang baik, seperti penggunaan *models-view-template* (MVT), yang mengajarkan bagaimana memisahkan logika bisnis, tampilan, dan data secara rapi. Dengan begitu, Django menjadi pilihan tepat untuk memulai pembelajaran karena memudahkan pemahaman konsep, memberikan alat yang lengkap, dan membantu membangun kebiasaan kode yang terstruktur.




V. Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek dalam kode Python dengan tabel-tabel di database relasional. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan konsep objek, tanpa perlu menulis perintah SQL secara langsung. Dengan ORM, setiap model dalam Django merepresentasikan sebuah tabel di database, dan atribut-atribut model tersebut menjadi kolom-kolom dalam tabel.

Misalnya, jika membuat model bernama `Product` dengan atribut `name`, `price`, dan `description`, Django secara otomatis mengubahnya menjadi tabel `Product` di database dengan kolom-kolom yang sesuai. ORM ini memudahkan pengelolaan data dalam aplikasi karena pengembang hanya perlu menggunakan kode Python untuk membuat, membaca, memperbarui, dan menghapus data. Ini membuat pengembangan lebih cepat dan mudah, serta mengurangi kemungkinan kesalahan dalam penulisan SQL.









### TUGAS 3

### Screenshot Postman
![alt text](XML_POSTMAN.png)
![alt text](JSON_POSTMAN.png)
![alt text](XML_ID_POSTMAN.png)
![alt text](JSON_ID_POSTMAN.png)




### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting karena ia memastikan data bisa dikirim dan diterima dengan baik antara server dan pengguna. Ini termasuk informasi yang dibutuhkan untuk menjalankan aplikasi, seperti data dari pengguna atau hasil pencarian. Jika data delivery tidak berfungsi dengan baik, aplikasi bisa lambat, mengalami kesalahan, atau bahkan tidak dapat mengirimkan informasi yang benar. Jadi, data delivery yang efektif membantu aplikasi bekerja dengan lancar dan memberikan pengalaman pengguna yang baik.




### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON umumnya dianggap lebih baik daripada XML untuk aplikasi web karena beberapa alasan utama. Pertama, JSON lebih ringkas dan sederhana dibandingkan XML, sehingga lebih mudah dibaca dan dipahami. Kedua, JSON mudah digunakan dalam berbagai bahasa pemrograman, terutama JavaScript, yang sering digunakan dalam pengembangan web. Ketiga, JSON sering lebih efisien, dengan sintaks yang lebih ringkas dan struktur yang lebih sederhana, JSON sering kali lebih cepat dalam hal kecepatan pemrosesan dan lebih hemat ruang penyimpanan. Karena kemudahan dan efisiensinya, JSON menjadi pilihan utama dalam banyak aplikasi web dan API.

JSON lebih populer karena kemudahan dan efisiensinya, yang membuatnya pilihan utama dalam banyak aplikasi web dan API.




### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` di Django digunakan untuk memastikan bahwa data yang dimasukkan ke dalam form sudah benar dan sesuai dengan aturan yang ditetapkan. Fungsi utama dari method ini adalah memeriksa setiap input data untuk memastikan bahwa data tersebut memenuhi semua kriteria validasi yang telah ditentukan, seperti format yang benar, panjang data yang sesuai, dan tidak adanya kesalahan lain. Dengan memanggil `is_valid()`, kita bisa memastikan bahwa hanya data yang valid dan sesuai yang diterima oleh aplikasi, sehingga mengurangi risiko kesalahan atau masalah yang bisa terjadi akibat data yang tidak benar. Method ini sangat penting karena membantu menjaga integritas data yang masuk ke aplikasi, memastikan bahwa aplikasi berfungsi dengan baik dan memberikan pengalaman pengguna yang lebih baik.




### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token (Cross-Site Request Forgery token) adalah fitur keamanan yang melindungi aplikasi web dari serangan yang bisa membahayakan pengguna. Bayangkan jika penyerang bisa membuat pengguna yang sedang login di sebuah situs web mengirimkan permintaan berbahaya tanpa mereka sadari, misalnya mengubah pengaturan akun mereka atau mengirimkan data yang tidak diinginkan. Tanpa CSRF token, aplikasi web tidak bisa membedakan apakah permintaan yang masuk berasal dari pengguna yang sah atau dari penyerang yang mencoba memanipulasi pengguna. Ini bisa menyebabkan masalah serius, seperti data yang salah atau kerusakan pada sistem.

CSRF token bekerja dengan cara memberikan setiap formulir atau permintaan yang dikirim dengan token unik yang hanya diketahui oleh aplikasi dan pengguna saat itu. Saat formulir dikirimkan, token ini juga dikirim bersama data lainnya. Aplikasi kemudian memeriksa token tersebut untuk memastikan permintaan itu benar-benar datang dari pengguna yang sah. Jika token tidak cocok atau tidak ada, permintaan ditolak. Ini membantu memastikan bahwa semua permintaan yang masuk adalah hasil dari tindakan yang sah dan menghindari serangan dari pihak yang tidak berwenang.




### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Implementasi Skeleton sebagai Kerangka Views
1. Buat Direktori templates: Di root folder proyek, buat direktori templates.
2. Buat Berkas base.html: Di dalam templates, buat berkas base.html dengan kode skeleton.
3. Sesuaikan Konfigurasi TEMPLATES di settings.py: Tambahkan BASE_DIR / 'templates' ke dalam DIRS dan pastikan APP_DIRS bernilai True.
4. Modifikasi Berkas main.html: Ubah berkas main.html di main/templates/ untuk me-extend base.html.

### Mengubah Primary Key Dari Integer Menjadi UUID
1. Hapus Berkas Basis Data: Jika objek sudah ada, hapus berkas db.sqlite3 untuk menghindari error.
2. Modifikasi models.py: Tambahkan import uuid di bagian atas dan ubah ID di model menjadi UUIDField dengan default=uuid.uuid4.
3. Jalankan Migrasi Model: jalankan python3 manage.py makemigrations dan python3 manage.py migrate.

### Membuat Form Input Data dan Menampilkan Data Mood Entry Pada HTML
1. Buat `forms.py`: Tambahkan `ProductForm` di `forms.py` untuk form data `Product`.
2. Modifikasi `views.py`: Tambahkan import dan fungsi `create_product_entry` untuk menangani input data dari form.
3. Update `show_main` di `views.py`: Modifikasi untuk menampilkan data `Product` di halaman utama.
4. Update `urls.py`: Tambahkan path URL untuk `create_product_entry`.
5. Buat `create_product_entry.html`: Buat template HTML untuk form input data `Product`.
6. Update `main.html`: Tambahkan kode untuk menampilkan data product dalam tabel dan tombol "Add New Product".
7. Jalankan Server**: Gunakan `python manage.py runserver` dan akses aplikasi di browser.

### Mengembalikan Data dalam Bentuk XML, JSON, XML berdasarkan id, JSON, berdasarkan id
1. Untuk XML:
   - Tambahkan import `HttpResponse` dan `serializers` di `views.py`.
   - Buat fungsi `show_xml` untuk mengembalikan data `Product` dalam format XML.
   - Tambahkan path URL `xml/` di `urls.py`.
2. Untuk JSON:
   - Buat fungsi `show_json` di `views.py` untuk mengembalikan data `Product` dalam format JSON.
   - Tambahkan path URL `json/` di `urls.py`.
3. Data Berdasarkan ID:
   - Buat fungsi `show_xml_by_id` dan `show_json_by_id` di `views.py` untuk mengembalikan data berdasarkan ID dalam format XML dan JSON.
   - Tambahkan path URL `xml/<str:id>/` dan `json/<str:id>/` di `urls.py`.
4. Jalankan Server:
   - Gunakan `python manage.py runserver` dan akses URL di browser sesuai dengan path yang telah ditambahkan.









### TUGAS 4

I. Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() dan redirect() adalah dua cara dalam Django untuk mengarahkan pengguna ke halaman lain, tetapi mereka berbeda dalam cara kerjanya. HttpResponseRedirect() adalah cara langsung untuk mengalihkan ke URL tertentu, di mana kamu harus menuliskan URL itu secara jelas, misalnya HttpResponseRedirect('/some-url/'). Sebaliknya, redirect() adalah cara yang lebih mudah dan fleksibel. Dengan redirect(), kamu bisa mengalihkan pengguna dengan hanya menyebutkan nama view, seperti redirect('some_view_name'), dan Django akan mencari URL yang sesuai secara otomatis.

Kelebihan dari redirect() adalah kemudahannya karena tidak perlu tahu URL secara pasti, cukup nama view-nya saja. Ini membuat kode lebih bersih dan mudah dibaca. Sementara itu, HttpResponseRedirect() memberi lebih banyak kontrol, tetapi lebih sulit digunakan karena kamu harus tahu URL yang tepat. Jadi, secara umum, redirect() lebih direkomendasikan karena lebih mudah dan lebih fleksibel.

Untuk menghubungkan model Product dengan model User dalam Django, kita dapat menggunakan relasi satu-ke-banyak (one-to-many). Ini berarti satu pengguna (User) dapat memiliki banyak produk (Product), tetapi setiap produk hanya dimiliki oleh satu pengguna. Berikut adalah langkah-langkah cara kerjanya:




II. Jelaskan cara kerja penghubungan model Product dengan User!

1. Pertama, kita perlu mendefinisikan model Product di file models.py. Di dalam model ini, kita akan menambahkan sebuah field yang merujuk ke model User. Kita menggunakan ForeignKey untuk membuat hubungan ini.

```from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name```

Pada contoh di atas, field user menggunakan ForeignKey untuk menghubungkan produk dengan pengguna. Parameter on_delete=models.CASCADE berarti jika pengguna dihapus, maka semua produk yang dimiliki oleh pengguna tersebut juga akan dihapus.

2. Ketika menyimpan produk baru, kita perlu menetapkan pengguna yang sedang login sebagai pemilik produk tersebut. Maka kita akan ubah code dalam views

```from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Mengaitkan produk dengan pengguna yang sedang login
            product.save()
            return redirect('product_list')  # Ganti dengan nama URL tujuan
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})```

Ketika kita membuat form di Django dan mengirimkannya, Django biasanya langsung menyimpan data yang diisi ke dalam database. Namun, terkadang kita ingin memodifikasi datanya terlebih dahulu sebelum benar-benar menyimpannya. Di sinilah commit=False berguna.

Biasanya, ketika form divalidasi dan disimpan dengan form.save(), Django langsung menyimpan data ke database. Saat kita menambahkan commit=False pada form.save(commit=False), Django tidak langsung menyimpan data ke database. Sebaliknya, Django hanya membuat objek dari form tersebut, tetapi tidak menyimpannya. Dalam kasus ini, kita menggunakan commit=False agar kita bisa menambahkan informasi tambahan ke objek sebelum menyimpannya ke database. Pada tugas e-commerce, objek yang ingin disimpan adalah produk (Product). Kita perlu menambahkan informasi siapa pemilik produk tersebut. Jadi, kita mengisi field user dengan request.user, yaitu pengguna yang sedang login. Setelah menambahkan informasi ini, baru kita menyimpan produk ke database menggunakan product.save().

3. Ubah show_main
Kode Product.objects.filter(user=request.user) akan menyaring semua data Product yang ada di database dan hanya mengambil data yang terhubung dengan pengguna yang sedang login. Django memanfaatkan request.user untuk mengetahui siapa pengguna yang sedang login, dan filter(user=request.user) akan membatasi hasilnya hanya untuk pengguna tersebut. Pada bagian context = {'name': request.user.username, ...}, nama pengguna yang login akan diambil dengan request.user.username dan disimpan dalam konteks. Kode ini memastikan bahwa nama pengguna (username) bisa ditampilkan di halaman, sehingga pengguna yang sedang login dapat melihat namanya sendiri.

```@login_required(login_url='/login')
def show_main(request):
    # Mengambil semua produk dari database yang ditambahkan oleh pengguna yang sedang login
    product_entries = Product.objects.filter(user=request.user)

    # Membuat konteks untuk template
    context = {
        'name': request.user.username,  # Nama pemilik
        'class': 'PBP B',  # Kelas
        'npm': '2306218111',  # NPM
        'product_entries': product_entries,  # Semua produk yang diambil dari database
        'last_login': request.COOKIES['last_login'],
    }

    # Render template 'main.html' dengan konteks yang sudah dibuat
    return render(request, "main.html", context)```

4. Migrasi Model

python manage.py makemigrations
python manage.py migrate

5. Mempersiapkan aplikasi web kita untuk environtment production. Untuk itu, tambahkan sebuah import baru pada settings.py 

import os

Kemudian, ganti variabel DEBUG dari berkas settings.py menjadi seperti ini.

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION




III.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication dan authorization adalah dua konsep yang berbeda tetapi saling berkaitan dalam keamanan aplikasi web. Authentication (otentikasi) adalah proses untuk memverifikasi identitas pengguna. Ketika seseorang login ke sebuah aplikasi, mereka memberikan kredensial seperti username dan password, dan sistem memeriksa apakah data tersebut cocok dengan yang ada di database. Jika cocok, pengguna dinyatakan terotentikasi. Sebaliknya, authorization (otorisasi) adalah proses untuk menentukan apakah pengguna yang sudah terverifikasi memiliki izin untuk mengakses atau melakukan tindakan tertentu. Misalnya, setelah login, pengguna biasa mungkin hanya bisa mengakses halaman profil mereka, sementara admin bisa mengelola konten atau pengguna lain.

Ketika seorang pengguna login, pertama-tama sistem akan melakukan otentikasi untuk memverifikasi identitasnya. Setelah pengguna berhasil terautentikasi, sistem akan melakukan otorisasi untuk memastikan pengguna memiliki hak akses yang sesuai dengan peran mereka. Dalam Django, sistem otentikasi bawaan sudah mencakup banyak fitur seperti login, logout, dan session management. Django menggunakan `request.user` untuk melacak pengguna yang sedang login, memungkinkan akses ke data pengguna di seluruh aplikasi. Django juga memiliki formulir otentikasi yang siap pakai, seperti `AuthenticationForm`, yang menangani input username dan password pengguna. Setelah login berhasil, Django menyimpan informasi pengguna dalam sesi untuk memastikan pengguna tetap terotentikasi selama sesi berlangsung.




IV. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login menggunakan cookies dan session. Ketika pengguna berhasil login, Django membuat sebuah session yang berisi informasi identitas pengguna, seperti `user_id`. Session ini kemudian dihubungkan dengan cookie yang disimpan di browser pengguna. Setiap kali pengguna melakukan request (seperti membuka halaman web lain), cookie tersebut dikirimkan bersama request untuk memberi tahu server bahwa pengguna sudah terotentikasi, sehingga tidak perlu login ulang selama sesi tersebut masih aktif.

Cookies adalah file kecil yang disimpan di browser pengguna dan memiliki beberapa kegunaan lain selain otentikasi, seperti:

1. Cookies dapat digunakan untuk mengingat pengaturan pengguna, seperti bahasa yang dipilih, tema, atau item dalam keranjang belanja di aplikasi e-commerce.
2. Cookies bisa digunakan untuk melacak aktivitas pengguna di berbagai halaman atau aplikasi untuk tujuan analitik atau iklan yang lebih personal.
3. Beberapa cookies menyimpan data sementara yang dibutuhkan untuk pengalaman pengguna yang lebih mulus saat menjelajah situs, seperti status login atau data input form yang belum dikirim.

Namun, tidak semua cookies aman digunakan. Ada beberapa risiko yang perlu diperhatikan:

1. Cookies yang menyimpan informasi sensitif (seperti login tokens atau data pribadi) tanpa enkripsi rentan terhadap serangan seperti **session hijacking**.
2. Cookies yang dibuat oleh pihak ketiga, seperti pengiklan, bisa digunakan untuk melacak pengguna di banyak situs web, yang dapat membahayakan privasi pengguna.
3. Jika sebuah situs web rentan terhadap XSS, seorang penyerang dapat menyuntikkan kode berbahaya yang bisa mencuri cookies pengguna. Untuk menghindari ini, cookie harus diatur dengan atribut **HttpOnly** dan **Secure** agar tidak dapat diakses melalui JavaScript dan hanya dikirim melalui koneksi HTTPS.

Jadi, meskipun cookies berguna untuk otentikasi dan menyimpan data pengguna, mereka harus dikelola dengan hati-hati untuk menghindari masalah keamanan.




V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat fungsi dan form registrasi dengan memodifikasi views.py dan import formulir bawaan dalam aplikasi web. Kemudian menambahkan fungsi register.
2. Membuat berkas register.html untuk menampilkan laman register dan menambahkan path url di urlpatterns
3. Setelah itu, saya lanjut membuat fungsi login dengan proses yang sama yaitu import fungsi bawaan django yaitu import authenticate, login, dan AuthenticationForm pada views.py . Kemudian, menambahkan fungsi login_user, membuat berkas login.html untuk membuat template laman untuk login dan melakukan url path untuk laman tersebut.
4. Saya lanjut dengan membuat fungsi logout dengan import logout pada views.py dan menambahkan fungsi view.py untuk melakukan mekanisme logout. Kemudian, saya memodifikasi berkas main.html untuk menambahkan hyperlink tag untuk logout. Lalu, saya menambahkan path url di url patterns untuk logout.
5. Setelah berhasil membuat form dan fungsi register, login, dan logout, saya lanjut merestriksi akses halaman main dengan import login_required. Saya juga menaruh @login_required(login_url='/login') agar halaman main hanya dapat diakses oleh pengguna yang sudah login.
6. Kemudian, saya lanjut setup agar bisa melihat data dari cookies. Hal ini dilakukan dengan menambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py. Saya juga memodifikasi fungsi login_user pada blok if form.is_valid() yang berfungsi untuk melakukan login terlebih dahulu, untuk membuat respose, dan membuat cookie last_login menambahkan ke response. Kemudian saya menambahkan variabel 'last_login': request.COOKIES['last_login'] pada context agar kita bisa melihat informasi cookie last_login pada web. Kemudian saya memodifikasi fungsi logout_user untuk menghapus cookie last_login saat pengguna melakukan logout. Saya kemudian menambahkan potongan kode last_login pada main.html untuk menampilkan informasi cookies di aplikasi web saya.
7. Untuk menghubungkan Model Product deengan User, saya mulai dengan import User pada models.py Kemudian, pada model Product yang sudah saya buat, saya menambahkan potongan kode seperti user = models.ForeignKey(User, on_delete=models.CASCADE) untuk menghubungkan satu product dengan satu user melalui sebuah relationship, dimana sebuah product pasti terasosiasikan dengan seorang user.
8. Saya kemudian membuka views.py dan memodifikasi create_product_entry seperti yang ada pada tutorial. Perubahan ini dilakukan untuk untuk membantu proses penyimpanan objek pada form ke user yang logged in.
9. Kemudian saya ubah value product_entries agar aplikasi hanya menambilkan objek Product yang terasosiakan dengan pengguna yang sedang login dan modifikasi pada context yaitu 'name': request.user.username, untuk menampilakn nama user yang sedang logged in.
10. Setelah itu, saya makemigrations dan migratesesuai dengan langkah yang ada pada tutorial.
11. Terakhir, saya buka settings.py untuk import os dan mengubah variabel DEBUG menjadi PRODUCTION = os.getenv("PRODUCTION", False) DEBUG = not PRODUCTION











### TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam pengembangan web, terdapat konsep yang dikenal sebagai CSS specificity. Ada beberapa cara untuk menghitung CSS specificity, baik dengan menggunakan selector maupun sistem angka desimal. Berikut adalah urutan prioritas selector CSS dari yang tertinggi hingga terendah:

- !important rule: Aturan ini memiliki prioritas tertinggi dan akan mengesampingkan semua aturan lainnya, termasuk inline style.
- Inline Style: Gaya yang diterapkan langsung pada elemen HTML melalui atribut style memiliki prioritas lebih tinggi daripada semua selector CSS lainnya.
- ID Selector (#): Selector ini diterapkan pada elemen yang memiliki atribut id.
- Pseudo-Class Selector (:). Selector ini diaplikasikan pada elemen dalam kondisi spesifik seperti :hover, :active, :nth-child()
- Attribute Selector ([]): Selector ini berdasarkan pada atribut yang terdapat dalam elemen HTML, contohnya [type="text"] atau [href].
- Class Selector (.): Selector ini menargetkan elemen yang memiliki atribut class dan memiliki prioritas lebih tinggi dibandingkan selector elemen.
- Element Type Selector: Selector ini mengacu pada tag HTML seperti div, p, h1, dan sebagainya.
- Universal Selector (*): Selector ini menargetkan semua elemen tanpa pengecualian.




2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Desain responsif telah menjadi konsep penting dalam pengembangan aplikasi web karena beberapa alasan berikut:

- Pengalaman Pengguna yang Lebih Baik: Pengalaman pengguna yang baik sangat penting, terutama jika aplikasi web digunakan untuk pemasaran. Dengan desain yang responsif, tampilan aplikasi dapat disesuaikan di berbagai perangkat, sehingga meningkatkan pengalaman pengguna dan reputasi merek.

- Perawatan yang Lebih Mudah: Dulu, pengembang harus membuat versi berbeda untuk setiap jenis perangkat. Namun, dengan desain responsif, satu situs dapat menyesuaikan tampilannya di semua perangkat, sehingga lebih mudah untuk dikelola.

- Waktu Muat yang Lebih Cepat: Sekitar 53% pengguna akan meninggalkan situs jika memuat lebih dari tiga detik. Desain responsif hanya memuat sumber daya yang diperlukan, sehingga situs dapat dimuat lebih cepat tanpa harus mengalihkan pengguna ke versi yang berbeda.

- Beragam Perangkat Saat Ini: Saat ini, aplikasi web diakses melalui berbagai perangkat, seperti ponsel, laptop, dan TV. Oleh karena itu, penting untuk memiliki desain responsif agar pengguna merasa nyaman saat mengakses aplikasi web.

Contoh aplikasi yang sudah menerapkan desain responsif: Tokopedia.
Contoh aplikasi yang belum menerapkan desain responsif: SIAKng.




3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Berikut adalah penjelasan dan contohnya masing - masing:

- Padding adalah ruang antara konten dan border, yang merupakan komponen berikutnya dari box. Kita bisa mengatur padding di setiap sisi. Contoh implementasinya adalah:
div {
    padding: 20px; /* Semua sisi akan diberi padding 20px */
    padding-top: 10px; /* Padding hanya pada bagian atas */
    padding-right: 15px; /* Padding hanya pada bagian kanan */
    padding-bottom: 10px; /* Padding hanya pada bagian bawah */
    padding-left: 15px; /* Padding hanya pada bagian kiri */
}

- Border adalah garis yang terlihat atau tidak terlihat di sekitar tepi box. Kita bisa mengatur ketebalannya, jenis border, dan warna border
div {
    border: 2px solid black; /* Border 2px tebal, jenis solid, warna hitam */
    border-top: 3px dashed red; /* Border atas saja dengan garis putus-putus merah */
}

- Margin adalah ruang luar di sekitar box yang mengatur jarak antara elemen dengan elemen lainnya.
div {
    margin: 20px; /* Semua sisi diberi margin 20px */
    margin-top: 10px; /* Margin hanya di bagian atas */
    margin-right: 15px; /* Margin hanya di bagian kanan */
    margin-bottom: 10px; /* Margin hanya di bagian bawah */
    margin-left: 15px; /* Margin hanya di bagian kiri */
}

- Untuk implementasi ketiga nya dalam satu class:
    <style>
        .box {
            margin: 30px;            
            padding: 20px;            
            border: 5px solid blue;   
            background-color: lightgray; 
        }
    </style>




4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

CSS Flexbox adalah metode tata letak satu dimensi yang berguna untuk mengatur dan menyelaraskan ruang antara item dalam sebuah kontainer grid. Flexbox dirancang agar dapat bekerja dengan berbagai jenis perangkat dan ukuran layar. Metode ini membuat desain dan pembuatan halaman web responsif menjadi lebih mudah, tanpa perlu banyak menggunakan properti float dan position dalam kode CSS.

Sementara itu, CSS Grid Layout adalah sistem tata letak dua dimensi yang menggunakan baris dan kolom. Metode ini sangat membantu untuk menciptakan tata letak yang lebih kompleks dan teratur.




5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Pertama, saya menambahkan tailwind ke aplikasi dengan memodifikasi file base.html dengan menambahkan tag <meta name="viewport"> dan <script src="https://cdn.tailwindcss.com">
- Setelah itu, saya menambahkan fitur Edit Product pada aplikasi. Saya mulai dengan modifikasi file views.py dan membuat fungsi baru bernama edit_product yang menerima parameter request dan id. Setelah itu, saya menambahkan import reverse dan HttpResponseRedirect.
- Kemudian, saya membuat file html baru yang dinamakan edit_product.html. Isi dari file ini dapat mengedit inputan dari form sebelumnya dengan struktur design / tampilan yang sama dengan create_product_entry.html. Setelah itu saya menambahkan path url pada urls.py.
- Setelah itu, saya menambahkan fitur hapus product pada aplikasi. Dengan cara menambahkan fungsi baru pada views.py seperti yang ada di tutorial dan melakukan path url yang baru.
- Saya kemudian menambahkan navigation bar pada aplikasi dengan membuat file html baru dinamakan navbar.html dengan text "Tekiee, "hello {{nama}}", dan log out button.
- Setelah membuat navbar.html, edit product, dan delete product, saya konfigurasi static files pada aplikasi dengan memodifikasi settings.py dan menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware' pada bagian MIDDLEWARE. Saya juga mengubah bagian STATIC_ROOT, TATICFILES_DIRS, dan STATIC_URL.
- Saya juga menambahkan global.css pada folder static/css yang berisi design css saya. Kemudian saya mengubah base.html agar style global.css dapat digunakan di Django.
- Lalu saya memodifikasi file login.html, register.html, create_product_entry menjadi styling tailwind. Untuk login.html saya menampilkan static image bernama sedih-banget.png yang akan ditampilkan sebelah login entry.
- Saya juga membuat file card_product.html yang akan menampilkan card baru untuk setiap product entry baru. Dan di dalam nya ada button untuk edit product dan delete product.
- Setelah menyelesaikan segala berkas html di template, saya akhirnya memodifikasi main.html agar segala berkas html lainnya dapat terintegrasi dengan baik.