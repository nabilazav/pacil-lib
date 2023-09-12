Link Aplikasi: https://pacil-lib-23.adaptable.app/main/ 

# Jelaskan bagaimana cara kamu mengimplementasikan checklist 

# Membuat proyek Django Baru
- Membuat direktori baru dengan nama "pacil_lib" dan masuk ke direktorinya.
- Mengaktifkan virtual environment dengan menjalakan perintah "python -m venv env"
- Membuat berkas "requirements.txt" dan tambahkan dependencies yang dibutuhkan oleh proyek Django. Lalu  jalankan "pip install -r requirements.txt".
- Membuat proyek Django dengan perintah "django-admin startproject pacil_lib ."
- Menambahkan "*" di ALLOWED_HOSTS pada berkas "settings.py" untuk mengizinkan akses dari semua host, sehingga memungkina aplikasi diakses secara luas.
- Menjalankan server Django dengan perintah "python manage.py runserver"
- Membuka http://localhost:8000 untuk memastikan proyek berhasil dibuat.
- Membuat repositori GitHub dengan nama "pacil-lib" yang public.
- Menambahkan berkas ".gitignore" untuk mengabaikan berkas-berkas yang tidak diperlukan.
- Lalu jalankan perintah git "init", "remote", "add", "commit" dan "push" ke repositori GitHub.

# Membuat aplikasi dengan nama main pada proyek tersebut.
- Membuka direktori pacil_lib, lalu aktifkan virtual environment
- Menjalankan perintah python manage.py startapp main untuk membuat aplikasi baru, lalu akan terbentuk direktori baru dengan nama main
- Membuka "settings.py" di dalam direktori pacil_lib
- Menambahkan "main" pada "INSTALLED_APPS"
- Membuat direktori templates di dalam direktori main
- Membuat file main.html di dalam direktori templates 

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
- Membuka file models.py pada direktori main dan tambahkan 
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
- Membuat migrasi model dengan menjalankan perintah "python manage.py makemigrations" untuk menciptakan file migrasi yang berisi perubahan model 
lalu jalankan "python manage.py migrate" untuk mengaplikasikan perubahan 

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
- Membuka views.py pada direktori main lalu tambahkan "from django.shortcuts import render" untuk mengimpor fungsi render dari modul django.shortcuts
- Menambahkan fungsi show_main yang menerima parameter request untuk menampilkan tampilan yang sesuai
- Membuka main.html pada direktori templates di direktori main lalu isi dengan sesuai ketentuan tugas 

#  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Membuat file urls.py pada direktori main
- Mengisi urls.py dengan 
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Kemudian pada direktori pacil_lib, buka file urls.py lalu impor "from django.urls import path, include"
- Menambahkan "path('main/', include('main.urls'))" untuk mengarahkan ke tampilan main dalam urlpatterns
- Menjalankan "python manage.py runserver" lalu buka http://localhost:8000/main/ untuk melihat page yang sudah dibuat

#  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Sign in menggunakan akun github, lalu deploy repo yang berisi project django tersebut, lalu pilih branch main 
- Pilih python app template, pilih postgreSQL
-Lalu pilih versi pyhton dan  pada bagian start command ketik (python manage.py migrate && gunicorn pacil_lib.wsgi)
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan tekan deploy app dan tunggu sampai selesai.



# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
Link Bagan: ristek.link/BaganPBP_NabilaZavira
Ketika ada permintaan (HTTP Request) kepada server web untuk mengakses sebuah situs, Django akan mencari URL yang sesuai di dalam file urls.py. Jika URL tersebut cocok, Django akan memanggil fungsi yang terhubung dengan URL tersebut di dalam views.py. Data diambil dari models.py serta untuk memperbarui data yang dibutuhkan. Lalu halaman HTML yang diminta akan ditampilkan sebagai http response.

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan agar tidak bercampur/berkonflik dengan versi lain python yang ada di sistem serta untuk mencegah konflik dan masalah antara proyek-proyek yang berbeda. Jika tidak menggunakan virtual environment, proyek-proyek dapat saling memengaruhi dan sulit untuk mengelola dependensi dengan baik. Kita dapat membuat aplikasi Django tanpa virtual environment, akan tetapi lebih baik jika Anda menggunakan virtual environment untuk menghindari konflik yang mungkin dapat terjadi

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
Model-View-Controller (MVC):
   - Model: representasi dari data dan logika bisnis dalam aplikasi. Model bertanggung jawab untuk mengelola data dan berinteraksi dengan database jika diperlukan.
   - View: Tampilan yang menampilkan data kepada pengguna dan menerima input dari pengguna.
   - Controller: Berperan sebagai perantara antara Model dan View. Controller mengambil input dari pengguna, memprosesnya, dan mengatur pembaruan pada Model atau View sesuai kebutuhan.

Model-View-Template (MVT):
   - Model: Model mewakili data dan logika bisnis aplikasi.
   - View: Tampilan yang menampilkan data kepada pengguna, tetapi sering terjadi pencampuran antara tampilan dan template. Template berisi HTML dengan kode template yang mengisi data dari model ke tampilan.
   - Template: berisi markup HTML dengan kode template yang mengatur data dari Model akan ditampilkan dalam tampilan.

Model-View-ViewModel (MVVM):
   - Model: Model menggambarkan data dan logika bisnis aplikasi.
   - View: Tampilan yang menampilkan data kepada pengguna.
   - ViewModel: Berfungsi sebagai perantara antara Model dan View. ViewModel mengubah data dari Model ke format yang cocok untuk tampilan, dan juga mengelola perintah atau tindakan yang berasal dari tampilan untuk dikirim kembali ke Model.

   Perbedaan utama dengan MVT dan MVVM: Dalam MVC, Controller memiliki peran sentral dalam mengelola aliran aplikasi dan berfungsi sebagai penghubung antara Model dan View.
   Perbedaan utama dengan MVC dan MVVM: MVT biasanya terkait dengan kerangka kerja Django dalam pengembangan web, dengan ciri khas penggunaan template dalam penyajian data.
   Perbedaan utama dengan MVC dan MVT: MVVM memisahkan tampilan dari logika bisnis dengan lebih kuat daripada MVC atau MVT. Dalam MVVM, ViewModel bertanggung jawab untuk mengatur data dan interaksi, sehingga tampilan dapat lebih independen dan mudah diuji.

