Link Aplikasi: https://pacil-lib-23.adaptable.app/main/ 

# Jelaskan bagaimana cara kamu mengimplementasikan checklist 

# Membuat proyek Django Baru

- Buat direktori baru dengan nama "pacil_lib" dan masuk ke direktorinya.
- Aktifkan virtual environment dengan menjalakan perintah "python -m venv env"

- Buat berkas "requirements.txt" dan tambahkan dependencies yang dibutuhkan oleh proyek Django. Lalu  jalankan "pip install -r requirements.txt".
- Buat proyek Django dengan perintah "django-admin startproject pacil_lib ."

- Tambahkan "*" di ALLOWED_HOSTS pada berkas "settings.py" untuk mengizinkan akses dari semua host, sehingga memungkina aplikasi diakses secara luas.
- Jalankan server Django dengan perintah "python manage.py runserver"
- Buka http://localhost:8000 di untuk memastikan proyek berhasil dibuat.

- Buat repositori GitHub dengan nama "pacil-lib" yang public.
- Tambahkan berkas ".gitignore" untuk mengabaikan berkas-berkas yang tidak diperlukan.
- Lalu jalankan perintah git "init", "remote", "add", "commit" dan "push" ke repositori GitHub.

# Membuat aplikasi dengan nama main pada proyek tersebut.

- Buka direktori pacil_lib, lalu aktifkan virtual environment
- Jalankan perintah python manage.py startapp main untuk membuat aplikasi baru, lalu akan terbentuk direktori baru dengan nama main
- Buka "settings.py" di dalam direktori pacil_lib
- Tambahkan "main" pada "INSTALLED_APPS"
- Buat direktori templates di dalam direktori main
- Buat file main.html di dalam direktori templates 

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib

- Buka file models.py pada direktori main dan isi dengan kode ini 
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
- Buat migrasi model dengan menjalankan perintah "python manage.py makemigrations" untuk menciptakan file migrasi yang berisi perubahan model 
lalu jalankan "python manage.py migrate" untuk mengaplikasikan perubahan 

#  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

- Buka views.py pada direktori main lalu tambahkan from django.shortcuts import render ntuk mengimpor fungsi render dari modul django.shortcuts

- Tambahkan fungsi show_main yang menerima parameter request untuk menampilkan tampilan yang sesuai

- Buka main.html pada direktori templates di direktori main lalu isi dengan sesuai ketentuan tugas 

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas

- Buat file urls.py pada direktori main
- Isi urls.py dengan 
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
- Kemudian pada direktori pacil_lib, buka file urls.py lalu impor "from django.urls import path, include"
- Tambahkan "path('main/', include('main.urls'))" untuk mengarahkan ke tampilan main dalam urlpatterns
- Jalankan "python manage.py runserver" lalu buka http://localhost:8000/main/ untuk melihat page yang sudah dibuat

#  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

- Sign in menggunakan akun github, lalu deploy repo yang berisi project django tersebut, lalu pilih branch main 
- Pilih python app template, pilih postgreSQL
-Lalu pilih versi pyhton dan  pada bagian start command ketik (python manage.py migrate && gunicorn pacil_lib.wsgi)
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan tekan deploy app dan tunggu sampai selesai.


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

Link Bagan: ristek.link/Bagan_NabilaZavira



- Virtual environment digunakan untuk mengisolasi paket dan dependensi dari aplikasi agar tidak bersinggungan dengan versi lain yang ada di komputer.
Penggunaan virtual environment membantu mengisolasi dependencies antara proyek-proyek yang berbeda.

 Definisikan model dalam berkas "models.py" pada aplikasi "main" untuk merepresentasikan produk.
- Buat dan terapkan migrasi model dengan perintah "makemigrations" dan "migrate."
- Buat template "main.html" untuk tampilan produk pada aplikasi "main."