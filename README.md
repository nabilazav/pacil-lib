Link Aplikasi: https://pacil-lib-23.adaptable.app/main/ 

# TUGAS 2
# Jelaskan bagaimana cara kamu mengimplementasikan checklist 

# Membuat proyek Django Baru
- Membuat direktori baru dengan nama "pacil_lib" dan masuk ke direktorinya.
- Mengaktifkan virtual environment dengan menjalakan perintah 
        python -m venv env
- Membuat berkas "requirements.txt" dan tambahkan dependencies yang dibutuhkan oleh proyek Django. Lalu  jalankan 
        pip install -r requirements.txt".
- Membuat proyek Django dengan perintah 
        django-admin startproject pacil_lib .
- Menambahkan "*" di ALLOWED_HOSTS pada berkas "settings.py" untuk mengizinkan akses dari semua host, sehingga memungkina aplikasi diakses secara luas.
- Menjalankan server Django dengan perintah 
        python manage.py runserver
- Membuka http://localhost:8000 untuk memastikan proyek berhasil dibuat.
- Membuat repositori GitHub dengan nama "pacil-lib" yang public.
- Menambahkan berkas ".gitignore" untuk mengabaikan berkas-berkas yang tidak diperlukan.
- Lalu jalankan perintah git "init", "remote", "add", "commit" dan "push" ke repositori GitHub.

# Membuat aplikasi dengan nama main pada proyek tersebut.
- Membuka direktori "pacil_lib", lalu aktifkan virtual environment
- Menjalankan perintah 
        python manage.py startapp main 
untuk membuat aplikasi baru, lalu akan terbentuk direktori baru dengan nama "main"
- Membuka "settings.py" di dalam direktori "pacil_lib"
- Menambahkan "main" pada "INSTALLED_APPS"
- Membuat direktori "templates" di dalam direktori "main"
- Membuat file "main.html" di dalam direktori "templates" 

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
- Membuka file "models.py" pada direktori "main" dan tambahkan 
        from django.db import models
        class Item(models.Model):
            name = models.CharField(max_length=255)
            date_added = models.DateField(auto_now_add=True)
            amount = models.IntegerField()
            description = models.TextField()
- Membuat migrasi model dengan menjalankan perintah 
        python manage.py makemigrations
untuk membuat file migrasi yang berisi perubahan model. Lalu jalankan 
        python manage.py migrate
untuk mengaplikasikan perubahan 

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
- Membuka "views.py" pada direktori main lalu tambahkan "from django.shortcuts import render" untuk mengimpor fungsi render
- Menambahkan fungsi "show_main" yang menerima parameter request untuk menampilkan tampilan yang sesuai
- Membuka "main.htm"l pada direktori "templates" di direktori "main" lalu isi dengan sesuai ketentuan tugas 

#  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Membuat file "urls.py" pada direktori "main"
- Mengisi "urls.py" dengan 
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]"

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Kemudian pada direktori "pacil_lib", buka file "urls.py" lalu impor 
        from django.urls import path, include
- Menambahkan "path('main/', include('main.urls'))" untuk mengarahkan ke tampilan main dalam "urlpatterns"
- Menjalankan 
        python manage.py runserver 
lalu buka http://localhost:8000/main/ untuk melihat page yang sudah dibuat

#  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Sign in menggunakan akun github, lalu deploy repo yang berisi project django tersebut, lalu pilih branch "main" 
- Pilih python app template lalu pilih postgreSQL
- Pilih versi pyhton yang digunakan dan pada bagian start command ketik
        python manage.py migrate && gunicorn pacil_lib.wsgi
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan klik deploy app dan tunggu sampai selesai.



# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
Link Bagan: ristek.link/BaganPBP_NabilaZavira
Ketika ada permintaan (HTTP Request) kepada server web untuk mengakses sebuah situs, Django akan mencari URL yang sesuai di dalam file "urls.py". Jika URL tersebut cocok, Django akan memanggil fungsi yang terhubung dengan URL tersebut di dalam "views.py". Data diambil dari "models.py" serta untuk memperbarui data yang dibutuhkan. Lalu halaman HTML yang diminta akan ditampilkan sebagai HTTP Response.

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


# TUGAS 3
#  Apa perbedaan antara form POST dan form GET dalam Django?
- POST berfungsi untuk mengirim data (file, data formulir, dll.) ke server web. POST mengembalikan kode status HTTP 201 jika data berhasil dibuat di server. Data dikirim dalam tubuh permintaan HTTP dan tidak terlihat di URL.
- GET berfungsi untuk membaca/mengambil data dari server web. GET mengembalikan kode status HTTP 200 (OK) jika data berhasil diambil dari server. Data dikirim melalui URL sebagai parameter query string.
- Dalam hal keamanan, POST lebih aman karena data tidak terlihat di URL. Sedangkan, GET kurang aman karena data terlihat di URL.
- Dalam hal ukuran data, POST cocok untuk data besar. Sedangkan, GET lebih cocok untuk data kecil.
- Dalam hal cacheability, POST tidak dapat di-cache. Sedangkan, GET dapat di-cache.
- Selain itu, POST dapat mengubah data. Sedangkan, GET tidak mengubah data.
Jadi, perbedaan utama adalah bahwa GET digunakan untuk membaca/mengambil data dari server dengan data yang terlihat di URL, sementara POST digunakan untuk mengirim data ke server dengan data yang tidak terlihat di URL. 

# Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML (eXtensible Markup Language):
- Digunakan untuk mengorganisasi dan menyimpan data dalam format yang terstruktur.
- Berfokus pada struktur data dan hierarki.
- Sering digunakan untuk pertukaran data antara sistem yang berbeda atau penyimpanan data terstruktur.
- Validasi data dapat diimplementasikan dengan mudah menggunakan skema XML.

JSON (JavaScript Object Notation):
- Digunakan untuk pertukaran data antara aplikasi, terutama dalam pengembangan web dan API.
- Format data yang sederhana, mudah dibaca oleh manusia, dan lebih ringkas daripada XML.
- Sering digunakan dalam komunikasi antara server dan klien dalam pengembangan web modern.
- Cocok untuk struktur data yang lebih fleksibel, seperti objek dan daftar.

HTML (HyperText Markup Language):
- Digunakan untuk merender dan menampilkan konten web di browser.
- Tidak cocok untuk pertukaran data terstruktur; tujuannya adalah untuk tampilan dan format halaman web.
- Menggunakan markup (tag) untuk mengatur tampilan dan hubungan antara elemen-elemen di halaman web.

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam aplikasi web modern karena simpel, mudah dibaca, ringan, dan kompatibel dengan JavaScript. JSON juga mendukung tipe data umum, dan mudah digunakan dalam berbagai bahasa pemrograman. Dengan fleksibilitas dalam struktur data dan kemampuan untuk embedding data, JSON menjadi format data yang ideal untuk berbagai keperluan pertukaran data di dunia web modern.

# Membuat input form untuk menambahkan objek model pada app sebelumnya
- Membuat file baru bernama "forms.py" pada direktori "main" untuk membuat form yang bisa menerima data item baru. Isi  dengan
        from django.forms import ModelForm
        from main.models import Item
        class ItemForm(ModelForm):
            class Meta:
                model = Item
                fields = ["name", "amount", "description"]
- Pada direktori "main" buka "views.py" dan menambahkan import 
        from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
- Membuat fungsi baru bernama "create_item" pada "views.py". Isi dengan
        def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_Item.html", context)
- Lalu ubah fungsi "show_main" pada "views.py" menjadi seperti ini
        def show_main(request):
            items = Item.objects.all()
            context = {
                'nama_aplikasi': 'Pacil Library',
                'nama': "Nabila Zavira",
                'kelas': "PBP D", 
                'items': items,
            }

            return render(request, "main.html", context)
- Pada direktori "main" buka "urls.py" dan import fungsi "create_item" 
        from main.views import show_main, create_item
- Menambahkan path url pada "urlpatterns" yang ada di "urls.py" pada direktori "main" supaya bisa mengakses fungsi yang sudah di-import sebelumnya 
        path('create-item', create_item, name='create_item')
- Membuat file baru bernama "create_item.html" pada direktori "main/templates". Isi dengan
        {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Item</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Item"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}"
- Lalu buka "main.html" dan tambahkan kode berikut supaya bisa menampilkan data produk dalam bentuk tabel dan juga ada tombol "Add New Item" yang akan redirect ke page form
        <table>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Description</th>
                <th>Date Added</th>
            </tr>

            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

            {% for item in items %}
                <tr>
                    <td>{{item.name}}</td>
                    <td>{{item.price}}</td>
                    <td>{{item.description}}</td>
                    <td>{{item.date_added}}</td>
                </tr>
            {% endfor %}
        </table>

        <br />

        <a href="{% url 'main:create_item' %}">
            <button>
                Add New Item
            </button>
        </a>

        {% endblock content %}"
    - Run project django dengan 
        python manage.py runserver
    dan buka http://localhost:8000 

# Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
- Pada direktori main buka "views.py" dan menambahkan import
        from django.http import HttpResponse
        from django.core import serializers
- Membuat fungsi bernama "show_xml" yang menerima parameter "request" dan membuat variabel bernama "data" untuk menyimpan hasil query dari seluruh data yang ada pada Item. Serta menambahkan return function berupa HTTPResponse yang berisi parameter data hasil query. 
- Membuat fungsi lain bernama "show_json", "show_xml_by_id", dan"show_json_by_id" seperti berikut
        def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
- Pada direktori "main", buka file "urls.py" dan import fungsi yang sudah dibuat pada step di atas. "from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id"
- Menambahkan path url pada "urlpatterns" yang ada di "urls.py" pada direktori "main" untuk mengakses fungsi yang sudah diimpor tadi
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'), 
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
- Run project django dengan 
        python manage.py runserver
dan buka http://localhost:8000/xml, http://localhost:8000/json, http://localhost:8000/xml/[id], http://localhost:8000/json/[id], 

Link SS Postman: ristek.link/Postman_NabilaZavira