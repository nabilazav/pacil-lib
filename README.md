Link Aplikasi: https://pacil-lib-23.adaptable.app/main/ 

# **TUGAS 2**
## Jelaskan bagaimana cara kamu mengimplementasikan checklist 

###  Membuat proyek Django Baru
- Membuat direktori baru dengan nama ```pacil_lib``` dan masuk ke direktorinya.
- Mengaktifkan virtual environment dengan menjalakan perintah 
```python -m venv env```
- Membuat berkas ```requirements.txt``` dan tambahkan dependencies yang dibutuhkan oleh proyek Django. Lalu  jalankan 
 ```pip install -r requirements.txt```
- Membuat proyek Django dengan perintah 
```django-admin startproject pacil_lib .```
- Menambahkan ```*``` di ALLOWED_HOSTS pada berkas ```settings.py``` untuk mengizinkan akses dari semua host, sehingga memungkina aplikasi diakses secara luas.
- Menjalankan server Django dengan perintah 
```python manage.py runserver```
- Membuka http://localhost:8000 untuk memastikan proyek berhasil dibuat.
- Membuat repositori GitHub dengan nama ```pacil-lib``` yang public.
- Menambahkan berkas ```.gitignore``` untuk mengabaikan berkas-berkas yang tidak diperlukan.
- Lalu jalankan perintah git ```init```, ```remote```, ```add```, ```commit``` dan ```push``` ke repositori GitHub.

### Membuat aplikasi dengan nama main pada proyek tersebut.
- Membuka direktori ```pacil_lib```, lalu aktifkan virtual environment
- Menjalankan perintah 
```python manage.py startapp main```
untuk membuat aplikasi baru, lalu akan terbentuk direktori baru dengan nama ```main```
- Membuka ```settings.py``` di dalam direktori ```pacil_lib```
- Menambahkan ```main``` pada ```INSTALLED_APPS```
- Membuat direktori ```templates``` di dalam direktori ```main```
- Membuat file ```main.html``` di dalam direktori ```templates```

### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
- Membuka file ```models.py``` pada direktori ```main``` dan tambahkan 
 ```python
    from django.db import models
    class Item(models.Model):
        name = models.CharField(max_length=255)
        date_added = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
        description = models.TextField()
```
- Membuat migrasi model dengan menjalankan perintah 
```python manage.py makemigrations```
untuk membuat file migrasi yang berisi perubahan model. Lalu jalankan 
```python manage.py migrate```
untuk mengaplikasikan perubahan 

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
- Membuka ```views.py``` pada direktori main lalu tambahkan 
```from django.shortcuts import render``` untuk mengimport fungsi render
- Menambahkan fungsi ```show_main``` yang menerima parameter request untuk menampilkan tampilan yang sesuai
- Membuka ```main.html``` pada direktori ```templates``` di direktori ```main``` lalu isi dengan sesuai ketentuan tugas 

###  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Membuat file ```urls.py``` pada direktori ```main```
- Mengisi ```urls.py``` dengan 
```python
from django.urls import path
from main.views import show_main
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
        ]"
```

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Kemudian pada direktori ```pacil_lib```, buka file ```urls.py``` lalu import
```from django.urls import path, include```
- Menambahkan ```path('main/', include('main.urls'))``` untuk mengarahkan ke tampilan main dalam ```urlpatterns```
- Menjalankan 
```python manage.py runserver```
lalu buka http://localhost:8000/main/ untuk melihat page yang sudah dibuat

###  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Sign in menggunakan akun github, lalu deploy repo yang berisi project django tersebut, lalu pilih branch ```main```
- Pilih python app template lalu pilih postgreSQL
- Pilih versi pyhton yang digunakan dan pada bagian start command ketik
```python manage.py migrate && gunicorn pacil_lib.wsgi```
- Masukkan nama app sesuai keinginan
- Centang bagian HTTP Listener on PORT dan klik deploy app dan tunggu sampai selesai.



## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
- Link Bagan: (ristek.link/BaganPBP_NabilaZavira)
- Ketika ada permintaan (HTTP Request) kepada server web untuk mengakses sebuah situs, Django akan mencari URL yang sesuai di dalam file "urls.py". Jika URL tersebut cocok, Django akan memanggil fungsi yang terhubung dengan URL tersebut di dalam "views.py". Data diambil dari "models.py" serta untuk memperbarui data yang dibutuhkan. Lalu halaman HTML yang diminta akan ditampilkan sebagai HTTP Response.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan agar tidak bercampur/berkonflik dengan versi lain python yang ada di sistem serta untuk mencegah konflik dan masalah antara proyek-proyek yang berbeda. Jika tidak menggunakan virtual environment, proyek-proyek dapat saling memengaruhi dan sulit untuk mengelola dependensi dengan baik. Kita dapat membuat aplikasi Django tanpa virtual environment, akan tetapi lebih baik jika Anda menggunakan virtual environment untuk menghindari konflik yang mungkin dapat terjadi

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
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


# **TUGAS 3**
##  Apa perbedaan antara form POST dan form GET dalam Django?
- POST berfungsi untuk mengirim data (file, data formulir, dll.) ke server web. POST mengembalikan kode status HTTP 201 jika data berhasil dibuat di server. Data dikirim dalam tubuh permintaan HTTP dan tidak terlihat di URL.
- GET berfungsi untuk membaca/mengambil data dari server web. GET mengembalikan kode status HTTP 200 (OK) jika data berhasil diambil dari server. Data dikirim melalui URL sebagai parameter query string.
- Dalam hal keamanan, POST lebih aman karena data tidak terlihat di URL. Sedangkan, GET kurang aman karena data terlihat di URL.
- Dalam hal ukuran data, POST cocok untuk data besar. Sedangkan, GET lebih cocok untuk data kecil.
- Dalam hal cacheability, POST tidak dapat di-cache. Sedangkan, GET dapat di-cache.
- Selain itu, POST dapat mengubah data. Sedangkan, GET tidak mengubah data.
Jadi, perbedaan utama adalah bahwa GET digunakan untuk membaca/mengambil data dari server dengan data yang terlihat di URL, sementara POST digunakan untuk mengirim data ke server dengan data yang tidak terlihat di URL. 

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
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

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam aplikasi web modern karena simpel, mudah dibaca, ringan, dan kompatibel dengan JavaScript. JSON juga mendukung tipe data umum, dan mudah digunakan dalam berbagai bahasa pemrograman. Dengan fleksibilitas dalam struktur data dan kemampuan untuk embedding data, JSON menjadi format data yang ideal untuk berbagai keperluan pertukaran data di dunia web modern.

## Membuat input form untuk menambahkan objek model pada app sebelumnya
- Membuat file baru bernama ```forms.py``` pada direktori ```main``` untuk membuat form yang bisa menerima data item baru. Isi  dengan
``` python
from django.forms import ModelForm
from main.models import Item
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
- Pada direktori ```main``` buka ```views.py``` dan menambahkan import 
```python
from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
```
- Membuat fungsi baru bernama ```create_item``` pada ```views.py```. Isi dengan
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_Item.html", context)
```
- Lalu ubah fungsi ```show_main``` pada ```views.py``` menjadi seperti ini
```python
def show_main(request):
    items = Item.objects.all()
    context = {
        'nama_aplikasi': 'Pacil Library',
        'nama': "Nabila Zavira",
        'kelas': "PBP D", 
        'items': items,
    }

    return render(request, "main.html", context)
```
- Pada direktori ```main``` buka ```urls.py``` dan import fungsi ```create_item``` 
```from main.views import show_main, create_item```
- Menambahkan path url pada ```urlpatterns``` yang ada di ```urls.py``` pada direktori ```main``` supaya bisa mengakses fungsi yang sudah di-import sebelumnya 
```path('create-item', create_item, name='create_item')```
- Membuat file baru bernama ```create_item.html``` pada direktori ```main/templates```. Isi dengan
```html
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
```
- Lalu buka ```main.html``` dan tambahkan kode berikut supaya bisa menampilkan data item dalam bentuk tabel dan juga ada tombol ```Add New Item``` yang akan redirect ke page form
```html
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

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
```
- Run project django dengan 
```python manage.py runserver```
dan buka http://localhost:8000 

## Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
- Pada direktori main buka ```views.py``` dan menambahkan import
```from django.http import HttpResponse```
```from django.core import serializers```
- Membuat fungsi bernama ```show_xml``` yang menerima parameter ```request``` dan membuat variabel bernama ```data``` untuk menyimpan hasil query dari seluruh data yang ada pada Item. Serta menambahkan return function berupa HTTPResponse yang berisi parameter data hasil query. 
- Membuat fungsi lain bernama ```show_json```, 
```show_xml_by_id```, dan```show_json_by_id``` seperti berikut
```python
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
```
## Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
- Pada direktori ```main```, buka file ```urls.py``` dan import fungsi yang sudah dibuat pada step di atas. ```from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id```
- Menambahkan path url pada ```urlpatterns``` yang ada di ```urls.py``` pada direktori ```main ```untuk mengakses fungsi yang sudah diimport tadi
```python
path('xml/', show_xml, name='show_xml'), 
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
```
- Run project django dengan 
 ```python manage.py runserver```
dan buka http://localhost:8000/xml, http://localhost:8000/json, http://localhost:8000/xml/[id], http://localhost:8000/json/[id], 

Link SS Postman: (ristek.link/Postman_NabilaZavira) 


# **TUGAS 4**
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
- UserCreationForm adalah form bawaan Django untuk membuat akun pengguna.
- Kelebihan dari menggunakan UserCreationForm yaitu:
    - UserCreationForm sudah termasuk dalam Django's built-in authentication system, tidak perlu membuat formulir pendaftaran pengguna dari awal sehingga mudah digunakan dan menghemat waktu.
    - Form ini terintegrasi dengan baik dengan sistem autentikasi Django, yang berarti setelah pengguna mendaftar, akun mereka dapat dengan mudah dikelola, seperti login, logout, reset kata sandi, dan lainnya.
    - Form ini mencakup validasi bawaan untuk memastikan bahwa pengguna memasukkan data yang valid saat mendaftar, seperti memeriksa apakah alamat email unik, mengonfirmasi kata sandi, dan lainnya.

- Kekurangan yang perlu diperhatikan:
    - Meskipun UserCreationForm sangat berguna untuk kasus penggunaan umum, tetapi tidak cukup fleksibel jika memerlukan custom yang lebih canggih atau perlu mengintegrasikan dengan basis data atau model pengguna yang kompleks.
    - Tampilan default yang dihasilkan oleh UserCreationForm mungkin terlihat sederhana dan kurang menarik. 
    - Jika memerlukan fitur pendaftaran yang lebih kompleks, seperti konfirmasi email, atau integrasi dengan layanan pihak ketiga, maka perlu menulis kode tambahan untuk mengimplementasikannya.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi adalah proses memverifikasi identitas pengguna yakni untuk mengidentifikasi siapa pengguna yang mencoba mengakses aplikasi web. Autentikasi digunakan untuk memeriksa apakah pengguna yang mencoba mengakses aplikasi adalah pengguna yang sah atau bukan. Ini memastikan bahwa hanya pengguna yang terdaftar dan terotentikasi yang dapat mengakses bagian tertentu dari aplikasi.
    - Contoh: Login adalah contoh autentikasi. Ketika pengguna memasukkan kredensial mereka (seperti nama pengguna dan kata sandi), sistem memverifikasi apakah kredensial tersebut sesuai dengan yang ada dalam basis data. Jika cocok, pengguna dianggap terotentikasi dan dapat mengakses sumber daya yang terlindungi.
- Otorisasi adalah proses mengendalikan akses pengguna yang sudah terotentikasi ke sumber daya atau fungsi tertentu dalam aplikasi. Ini menentukan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna yang terotentikasi. Otorisasi mengontrol hak akses pengguna. Ini memastikan bahwa bahkan setelah terotentikasi, pengguna hanya memiliki akses ke bagian-bagian tertentu dari aplikasi yang sesuai dengan peran dan izin mereka.
    - Contoh: Seorang pengguna yang terotentikasi mungkin memiliki izin untuk mengedit profil mereka sendiri, tetapi tidak diberi izin untuk mengedit profil pengguna lain. Ini adalah contoh dari otorisasi yang mengatur apa yang dapat dilakukan pengguna setelah mereka masuk.

- Autentikasi dan otorisasi bekerja bersama-sama untuk menjaga keamanan aplikasi web. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sedangkan otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan izin mereka. Otorisasi memungkinkan pengembang untuk mengontrol tingkat privasi pengguna dan data dalam aplikasi untuk melindungi informasi sensitif dan menjaga integritas aplikasi. Otorisasi memungkinkan pengembang untuk mengelola akses pengguna secara efektif, termasuk pengaturan peran, izin, dan hak akses yang memungkinkan pengaturan tingkat akses yang tepat untuk setiap pengguna.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
- Cookies adalah sejumlah kecil informasi yang dikirim oleh server web ke browser dan kemudian dikirim kembali oleh peramban pada page request yang akan datang. 
- Dalam Django, cookies digunakan khususnya untuk mengelola data sesi pengguna. Mereka membuat dan menyimpan cookie sesi, mengirimkannya ke server saat pengguna berinteraksi dengan situs web, dan digunakan untuk mengidentifikasi dan menyimpan data sesi pengguna. Penggunaan cookies memungkinkan pengalaman pengguna yang lebih baik, meskipun harus memperhatikan masalah keamanan seperti serangan XSS.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- Penggunaan cookies dalam pengembangan web dapat aman jika diimplementasikan dengan benar dan dengan mempertimbangkan berbagai risiko potensial, termasuk serangan XSS, pencurian data, pencurian cookies, pemantauan, dan blokir oleh pengguna. Untuk menjaga keamanan cookies, Anda harus mengamankannya dengan HTTPS, menggunakan atribut HttpOnly dan Secure, validasi data dengan hati-hati, enkripsi data sensitif, dan mematuhi regulasi privasi yang berlaku.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
#### Register
- Pertama-tama jalankan virtual environment
- Lalu membuka ```views.py``` yang ada di directory ```main``` dan menambahkan import ```redirect```, ```UserCreationForm```, dan ```messages```
- Membuat fungsi yang bernama ```register``` yang menerima parameter ```request```
``` python
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
```
- Membuat file HTML baru yang bernama ```register.html``` pada folder ```main/templates``` Isi dengan
``` html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
- Lalu membuka ```urls.py``` yang ada pada folder ```main``` dan import ``` form main.views import register``` dan menambahkan path url ke dalam ```urlpatterns``` untuk mengakses fungsi yang sudah diimport
```path('register/', register, name='register'),```

#### Login
- Membuka ```views.py``` yang ada pada folder ```main``` dan menambahkan import ```authenticate``` dan ```login``` yaitu
```from django.contrib.auth import authenticate, login```
- Buat fungsi yang bernama ```login_user``` yang menerima parameter ```request``` 
``` python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
- Membuat file html baru yang bernama ```login.html``` pada folder ```main/templates``` Isis dengan
``` html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
- Lalu membuka ```urls.py``` yang ada pada ```main``` dan import  ```from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat``` lalu menambahkan path url ke ```urlpatterns``` untuk mengakses fungsi yang sudah diimport ```path('login/', login_user, name='login'),```

#### Logout
- Membuka ```views.py``` yang ada di folder ```main``` lalu menambahkan import ```logout``` yaitu ```from django.contrib.auth import logout```
- Membuat fungsi yang bernama ```logout_user```yang menerima paramter ```request```
``` python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- Lalu membuka file ```mian.html``` yang ada pada folder ```main/templates``` kemudian menambahkan kode berikut setelah tag Add New Item pada ```main.html```
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
- Membuka ```urls.py``` yang ada pada folder ```main``` dan import ```from main.views import logout_user``` daan menambahkan path url ke ```urlpatterns``` yaitu ```path('logout/', logout_user, name='logout'),```

### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- Membuat 2 akun pengguna (yang pertama dengan username Nabila dan yang kedua dengan username Bella)
- Pada akun Nabila melakukan add new item sebanyak 3 kali 
- Pada akun Bella melakukan add new item sebanyak 3 kali juga
- Sehingga pada masing masing akun sekarang memiliki 3 dummy data

(ristek.link/DummyData_NabilaZavira)

### Menghubungkan model Item dengan User.
- Membuka ```models.py``` yang ada pada ```main```  lalu import
```from django.contrib.auth.models import User```
- Kemudian tambahkan kode pada Item yang sudah dibuat
``` python
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
- Membuka ```views.py``` yang ada pada ```main``` lalu ubah potongan kode pada fungsi ```create_item```
``` python
def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
 ```
 - Kemudian ubah fungsi ```show_main```
 ```python
 def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```
- Setelah save semua perubahan, lalu melakukan migrasi model dengan````python manage.py makemigrations```. Kemudian pilih 1 untuk menetapkan default value untuk field user, lalu ketik 1 lagi untuk menetapkan user dengan ID 1 yang sudah dibuat sebelumnya.
- Kemudian jalankan perintah ```python manage.py migrate```

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
- Membuka ```views.py``` yanga ada pada main lalu tambahkan import 
``` python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- Kemudian pada fungsi ```login_user```, mengganti kode pada ``` if user is not None``` menjadi 
``` python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
untuk menambahkan cookie yang memiliki nama last_login
- Lalu pada fungsi ```show_main```, menambahkan kode pada variabel ```context```
``` python
context = {
    'name': 'Pak Bepe',
    'class': 'PBP A',
    'items': items,
    'last_login': request.COOKIES['last_login'],
}
```
- Mengubah fungsi logout_user menjadi 
``` python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- Kemudian membuka file ```main.html``` lalu menambahkan kode di antara tabel dan tombol logout
``` html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
- Lalu menjalankan perintah ```python manage.py runserver```


# **TUGAS 5**
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

- Element Selector (tanpa diawali # or .) memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. Jadi bisa mengaplikasikan style pada semua elemen dalam dokumen, perlu hati-hati karena dapat mempengaruhi semua elemen.
- Class Selector (with leading .) memilih elemen berdasarkan nama class, untuk menerapkan style khusus pada elemen yang memiliki class tertentu.
- ID Selector (diawali dengan #) memilih elemen berdasarkan ID, digunakan untuk mengidentifikasi elemen unik dan menerapkan gaya atau fungsi khusus.
- Type Selector (tag selector) memilih semua elemen dengan tag tertentu, seperti p untuk semua paragraf, digunakan ketika ingin menerapkan style umum pada semua elemen dengan tag yang sama.
- Attribute Selector ([attribute=value]) memilih elemen berdasarkan atribut dan nilainya, digunakan untuk menerapkan gaya pada elemen dengan atribut tertentu, misalnya input[type="text"]
- Pseudo-class Selector (:pseudo-class) memilih elemen berdasarkan kondisi atau status tertentu, seperti :hover untuk mengganti tampilan saat mouse mengarah ke atas elemen, digunakan untuk mengubah tampilan interaktif.
- Pseudo-element Selector (::pseudo-element) memilih bagian tertentu dari elemen, seperti ::before untuk menambahkan konten sebelum elemen, digunakan untuk menambahkan elemen virtual ke dalam dokumen.
Waktu yang tepat untuk menggunakannya tergantung pada kebutuhan dan situasi

## Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 memperkenalkan banyak tag baru, beberapa di antaranya adalah:

- `<header>` : menandakan bagian atas dari sebuah dokumen atau bagian dari konten.
- `<nav>`: mengelompokkan tautan navigasi.
- `<section>`: mengelompokkan konten dalam sebuah dokumen.
- `<article>`: mendefinisikan sebuah artikel independen dalam dokumen.
- `<footer>`: menandakan bagian bawah dari sebuah dokumen atau bagian dari konten.
- `<aside>`: menunjukkan konten yang terkait, tetapi bukan bagian utama dari dokumen.

## Jelaskan perbedaan antara margin dan padding.
- Margin adalah space kosong di sekitar border. Margin memengaruhi jarak antara elemen dengan elemen lain di luarnya. Margin digunakan untuk mengatur jarak antara satu elemen dengan elemen elemen lainnya yang berada di sisi luar element.
- Padding adalah space kosong di sekitar konten. Padding memengaruhi jarak antara konten elemen dan border elemen itu sendiri. Margin Padding untuk mengatur jarak antara satu elemen dengan border elemen (yang berada di sisi dalam element).

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
- Tailwind CSS membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. Sedangkan, Bootstrap menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.
- Tailwind CSS memiliki file CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada. Sedangkan, Bootstrap memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena termasuk banyak komponen yang telah didefinisikan.
- Tailwind CSS memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek. Sedangkan, Bootstrap sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
- Tailwind CSS memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan. Sedangkan, Bootstrap memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.

Pemilihan antara Bootstrap dan Tailwind tergantung pada kebutuhan:
- Tailwind CSS lebih cocok jika memerlukan fleksibilitas tinggi, bekerja pada proyek khusus dengan tampilan yang unik, dan memiliki waktu untuk memahami kelas-kelas utilitas yang tersedia.
- Bootstrap lebih cocok jika perlu menjaga konsistensi desain di seluruh proyek, merupakan seorang pemula dalam pengembangan web, atau jika ingin membangun proyek dengan cepat, atau membutuhkan dukungan yang kuat dari komunitas dan dokumentasi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Menambahkan bootstrap ke aplikasi
- Membuka file base.html pada templates folder yang berada di root project. Pada templates/base.html, tambahkan tag `<meta name="viewport">` agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile (apabila belum).
``` html
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```
- Menambahkan Bootstrap CSS dan juga JS.
``` html
{% load static %}
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```
### Menambahkan navbar pada Aplikasi
- Menambahkan navigation bar (menggunakan Bootstrap) pada halaman main.html dar (getbootstrap.com)
- Lalu pada navbar saya ubah dengan memberikan button logout dan juga mengubah warnanya
``` html
 <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link logout-button" href="{% url 'main:logout' %}">Logout</a>
             </a>
            </li>
        </ul>
```
```css
  .logout-button {
            background-color: #d63b0c; /* Warna latar belakang */
            color: #FFFFFF; /* Warna teks */
            border: 2px solid #ead6d2; /* Warna border */
            border-radius: 10px; /* Sudut border */
            margin-left: 10px;
        }

```
### Menambahkan fitur edit pada aplikasi
- Membuka views.py yang ada pada folder main, dan buatlah fungsi baru bernama edit_item yang menerima parameter request dan id.
``` python
def edit_item(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)
```
- Buatlah file HTML baru dengan nama edit_item.html pada folder main/templates. Isi berkas tersebut dengan template berikut.
``` html
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
- Membuka urls.py yang berada pada folder main dan import fungsi edit_item yang sudah dibuat.
- Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimport tadi.
``` python
path('edit-item/<int:id>', edit_item, name='edit_item'),
```

### Membuat fungsi untuk menghapus data item
- Membuat fungsi baru dengan nama delete_item yang menerima parameter request dan id pada views.py di folder main untuk menghapus data item. 
```python
def delete_item(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Membuka urls.py yang ada pada folder main dan import fungsi yang sudah dibuat tadi.
``` python
from main.views import delete_item
```
- Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimport.
``` python
path('delete/<int:id>', delete_item, name='delete_item'), 
```

### Membuat fungsi menambahkan/mengurangkan amount
- Membuat fungsi baru dengan nama delete_item yang menerima parameter request dan id pada views.py di folder main untuk menghapus data item. 
``` python
def increase_amount(request, id):
    item = Item.objects.get(pk = id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_amount(request, id):
    item = Item.objects.get(pk = id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    if item.amount == 0:
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Membuka urls.py yang ada pada folder main dan import fungsi yang sudah dibuat tadi.
```python
from main.views import increase_amount,decrease_amount
```
- Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimport.
```python
path('increase_amount/<int:id>/', increase_amount name='increase_amount'),
path('decrease_amount/<int:id>/', decrease_amount, name='decrease_amount'),
```

### Menambahkan gambar
- Pada file settings.py yang berada pada folder pacil_lib, tambahkan kode
``` python
import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),
]
```
- Lalu menyimpan foto yang ingin digunakan pada folder main/static dan tambahkan 
`{% load static %}` pada file yang akan ditambahkan gambar
- Pada `login.html` menambahkan foto pada body
``` css
        background-image: url("{% static 'lib.jpg' %}");
```
- Pada `main.html` menambahkan foto pada card
```html
            <img src="{% static 'image.jpg' %}" alt="Image">
```

### Mengatur tampilan dengan css pada file `register.html`, `edit_item.html`, `create_item.html`
``` css
<head>
    <style>
        h1 {
            text-align: center; /* Pusatkan teks horizontal */
            margin-bottom: 30px;
            margin-top: 15px;
            font-family: 'Poppins';
        }
        body{
            background-color: #d8bfcf;
        }
        form {
            max-width: 500px; /* Atur lebar maksimum form */
            margin: 0 auto; /* Pusatkan form horizontal */
            padding: 20px; 
            border-radius: 20px; /* Tambahkan sudut bulat pada form */
            background-color: #efe8ef; /* Atur latar belakang form */
        }
    
        table {
            width: 100%;
        }
    
        table tr td {
            padding: 10px; /* Tambahkan padding pada sel form */
        }
    
        input[type="submit"] {
            background-color: #8d3b6b; /* Atur warna latar belakang tombol */
            color: #FFFFFF; /* Atur warna teks tombol */
            border: 2px solid #dad1db; /* Atur border tombol */
            border-radius: 10px; /* Tambahkan sudut bulat pada tombol */
            padding: 10px 20px; /* Tambahkan padding pada tombol */
            display: block; /* Ubah tombol menjadi elemen blok agar teksnya di tengah */
        }
        
    </style>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
```
### Mengatur tampilan pada `login.html`
- Memberikan teks PACIL LIB. dan di style pada .container{} dan h1{} supaya teks nya di center top, dan mengatur font teks
- Mengatur border login agar di center dengan .login{} dan mengatur button login dengan .login_btn{} dan login_btn:hover{}
``` css
{% load static %}
<head>
<style>
     .container {
        display: flex;
        flex-direction: column;
        justify-content: center; /* vertikal */
        align-items: center; /*  horizontal */
        height: 100vh;

    }
    body {
        display: flex;
        place-items: center start;
        font-family: 'Poppins';
        background-image: url("{% static 'lib.jpg' %}");
        background-size: cover;
        
    }

    h1 {
        font-weight: bold; 
        text-align: center; /* Teks menjadi terpusat secara horizontal */
        color: #3d154e;
        position: absolute;
        top: 50px; /* Menggeser elemen ke atas */
        left: 50%; /* Memposisikan elemen secara horizontal di tengah */
        transform: translate(-50%, 0);
        font-size:75px;

    }
    .login {
        background-color: rgb(244, 236, 255);
        padding: 50px;
        border-radius: 100px;
        position: absolute;
        top: 50%; /* Menggeser elemen ke tengah vertikal */
        left: 50%; /* Memposisikan elemen secara horizontal di tengah */
        transform: translate(-50%, -50%); 
    }
    .login_btn {
        background-color: #e2bef9; /* Warna latar belakang tombol */
        color: #383535; /* Warna teks */
        border: 2px solid #dad1db;
        border-radius: 5px;
        padding: 5px 15px;
        margin-top: 5px;
        margin-bottom: 10px;
        cursor: pointer; /* Ganti kursor saat di atas tombol */
    }

    .login_btn:hover {
        background-color: #a882c0; /* Warna latar belakang saat tombol dihover */
    }
</style>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

</head>

<div class="container">
        <h1>PACIL LIB.</h1>
       
    </div>

```

### Mengatur tampilan pada file `main.html`
- Menggunakan approach card, dan memberikan warna yang berbeda pada item yang terakhir di add dengan `{% if forloop.last %}`
``` html
<div class="row row-cols-1 row-cols-md-3 g-4">
    {% for item in items %}
    <div class="col">
        <div class="card h-100{% if forloop.last %} last-card{% endif %}">
            <!-- Menggunakan atribut src untuk menampilkan gambar -->
            <img src="{% static 'image.jpg' %}" alt="Image">
            
            <div class="card-body">
                <h5 class="card-title">{{ item.name }}</h5>
                <p class="card-text">{{ item.description }}</p>
                <p class="card-text">Amount: {{ item.amount }}</p>
                <p class="card-text">Date Added: {{ item.date_added }}</p>
            </div>
            <div class="card-footer">
                <a href="{% url 'main:increase_amount' item.pk %}" class="btn btn-secondary"style="margin-left: 5px;">+</a> {{item.amount}}
                <a href="{% url 'main:decrease_amount' item.pk %}" class="btn btn-secondary"style="margin-right: 30px;">-</a>
                <a href="{% url 'main:edit_item' item.pk %}" class="btn btn-primary"style="margin-right: 10px;">Edit</a>
                <a href="{% url 'main:delete_item' item.pk %}" class="btn btn-danger">Delete</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```
- Mengatur tampilan teks, posisi warna dan button seperti ini
``` css
<head>
    <style>
        h1 {
        font-weight: bold;
        text-align: center; /* Teks menjadi terpusat secara horizontal */
        margin-top: 10px;
        margin-bottom: 30px;

        }
        body {
            background-color: rgb(235, 215, 228);
            text-align: center;  /*Teks menjadi terpusat secara horizontal */
            margin-bottom: 30px;
            font-family: 'Poppins', sans-serif;
            
        }
        .navbar {
            background-color: #343a40; /* Warna latar belakang navbar */
        }

        .navbar-brand {
        font-weight: bold; 
        }
        .nav-link {
            color: #b09b9b; /* Warna teks */
        }

        .nav-link:hover {
            color: #7b687f; /* Warna teks saat dihover */
        }

        h1 {
            color: #343a40; /* Warna teks untuk judul utama */
        }

        h5 {
            color: #343a40; /* Warna teks untuk subjudul */
        }
        .card {
            background-color: #faf2f8; /* Warna latar belakang default card */
            margin: 10px; /* Tambahkan margin agar isi card tidak terlalu mepet dengan border */
            padding: 10px; /* Tambahkan padding agar isi card terlihat lebih rapi */
            border-radius: 15px; /* Atur border-radius untuk membuat card lebih bulat */
        }
        .card-container {
            justify-content: center; /* Pusatkan konten horizontal */
            align-items: center; /* Pusatkan konten vertikal */
        }
        .last-card {
            background-color: #f3f3e6;
            margin: 10px;
            padding: 10px;
        }
        .add-item {
            background-color: rgb(181, 57, 173);
            margin-top: 40px;
            margin-bottom: 40px;
            color: #FFFFFF; /* Warna teks */
            border: 2px solid #e8d9e2; /* Warna border */
            border-radius: 10px; /* Sudut border */
            padding: 5px 15px; /* Padding tombol */
        }
        .add-item:hover{
            background-color: rgb(135, 17, 128); 
        }
        .logout-button {
            background-color: #d63b0c; /* Warna latar belakang */
            color: #FFFFFF; /* Warna teks */
            border: 2px solid #ead6d2; /* Warna border */
            border-radius: 10px; /* Sudut border */
            margin-left: 10px;
        }

</style>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
</head>
```

# **TUGAS 6**
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronous Programming: tugas-tugas dieksekusi secara berurutan, satu per satu. Ketika sebuah tugas (misalnya, pemanggilan fungsi atau operasi jaringan) sedang berjalan, program akan berhenti dan menunggu hingga tugas tersebut selesai sebelum melanjutkan ke tugas berikutnya. 
- Asynchronous Programming: tugas-tugas dieksekusi secara simultan tanpa harus menunggu tugas sebelumnya selesai. Pemrograman asinkron memungkinkan program untuk menjalankan beberapa tugas secara bersamaan tanpa menghentikan eksekusi program utama.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah pendekatan di mana program merespons peristiwa atau kejadian tertentu yang terjadi dalam sistem atau aplikasi. Program ini biasanya memiliki daftar penanganan acara yang akan dijalankan ketika peristiwa tersebut terjadi. Contoh penerapan paradigma ini adalah dalam penggunaan event listener dalam JavaScript. Misalnya, menambahkan event listener ke elemen HTML sehingga ketika pengguna mengklik elemen tersebut, fungsi tertentu akan dieksekusi.

## Jelaskan penerapan asynchronous programming pada AJAX.
Dalam penerapan AJAX, asynchronous programming sangat penting. AJAX (Asynchronous JavaScript and XML) digunakan untuk mengirim permintaan ke server tanpa harus memuat ulang halaman web. Dengan memanfaatkan callback functions atau Promise dalam JavaScript, kita dapat membuat permintaan AJAX tanpa memblokir eksekusi program utama, sehingga halaman web tetap responsif.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
- Fetch API adalah API bawaan di JavaScript yang menyediakan interface untuk mengirim dan menerima permintaan HTTP secara asinkronus. Fetch API merupakan pendekatan modern yang lebih ringan dan terintegrasi dengan baik dalam JavaScript. Keuntungan Fetch API adalah ukuran yang lebih kecil, tidak perlu mengunduh library tambahan, dan dukungan untuk Promise.
- jQuery adalah library JavaScript yang memiliki banyak fitur dan sudah ada dalam pengembangan web selama beberapa tahun. jQuery menyediakan fungsi-fungsi yang nyaman untuk melakukan AJAX dan interaksi dengan DOM. Namun, ukurannya lebih besar daripada Fetch API, dan dalam proyek yang lebih besar, dapat menjadi overhead yang tidak perlu.

Pilihan antara keduanya tergantung pada kebutuhan proyek. Untuk proyek kecil atau ketika hanya membutuhkan AJAX sederhana, Fetch API adalah pilihan yang baik. Namun, jika sudah memiliki pengalaman dengan jQuery atau proyek nya membutuhkan banyak fitur jQuery lainnya, maka menggunakan jQuery juga bisa menjadi pilihan yang valid.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 ### AJAX GET (Ubahlah kode tabel data item agar dapat mendukung AJAX GET. Lakukan pengambilan task menggunakan AJAX GET.)
- Membuat fungsi baru pada `views.py` dengan nama `get_item_json` yang menerima parameter request. Fungsi ini akan digunakan untuk menampilkan data produk pada HTML dengan menggunakan `fetch`
```python
def get_item_json(request):
    item_product = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_product))
```

 ### AJAX POST (Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.)

Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.

### Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
- Membuat fungsi baru pada `views.py` dengan nama `add_item_ajax` yang menerima parameter request
```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()
```
- Melakukan import  ```from django.views.decorators.csrf import csrf_exempt``` pada berkas `views.py`

### Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
- Membuka file `urls.py` pada folder `main` dan import fungsi  `get_item_json` serta `add_item_ajax`

#### Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
- Menambahkan path url kedua fungsi tersebut ke dalam urlpatterns
``` python
path('get-item/', get_item_json, name='get_item_json'),
path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
```

### Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
- Membuka file `main.html` pada `main/templates` dan menghapus bagian kode cards yang sudah dibuat pada tutorial sebelumnya
- Menambahkan kode berikut sebagai struktur cards ```<div id="item_card" class="row g-2"> </div>```
- Membuat block `<Script>` di bagian bawah berkas kamu dan buatlah fungsi baru pada block `<Script>` tersebut dengan nama `getItems()`
```html
<script>
  async function getItems() {
    return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
  }
  <script>
```
- Membuat fungsi baru pada block `<Script>` dengan nama `refreshItems()` yang digunakan untuk me-refresh data produk secara asynchronous.
``` html
<script>
  async function refreshItems() {
    const items = await getItems();
    const itemCard = document.getElementById("item_card");
    itemCard.innerHTML = ""; // Kosongkan elemen sebelum menambahkan kartu

    items.forEach((item) => {
      const card = document.createElement("div");
      card.className = "col-md-2 col-6 card with-margin";

      card.innerHTML = `
      <div class="card h-100">          
        <img src="{% static 'image.jpg' %}" alt="Image">
          <div class="card-body">
            <h5 class="card-title">${item.fields.name}</h5>
            <p class="card-text">${item.fields.description}</p>
            <p class="card-text">Amount: ${item.fields.amount}</p>
            <p class="card-text">Date Added: ${item.fields.date_added}</p>
  
          </div>
        </div>
      `;

      itemCard.appendChild(card);
    });
    const lastCard = itemCard.lastElementChild;
    if (lastCard) {
      lastCard.classList.add("last-card");
    }
  }
  refreshItems();
  </script>
```
- Membuat modal sebagai form untuk menambahkan produk
``` html
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
            </div>
        </div>
    </div>
</div>

```
- Menambahkan button yang berfungsi untuk menampilkan modal
```html
<button type="button" class="btn btn-primary add-item" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Add Item by AJAX
</button>

```
- Membuat fungsi baru pada block `<Script>` dengan nama  `addItem()` 
```html
<script>
  function addItem() {
    fetch("{% url 'main:add_item_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#form'))
    }).then(refreshItems);

    document.getElementById("form").reset();
    return false;
  }
</script>
```
- Menambahkan fungsi onclick pada button "Add Item" pada modal untuk menjalankan fungsi `addItem()`
``` html
<script>
  document.getElementById("button_add").onclick = addItem;
</script>
```
### Melakukan perintah collectstatic.
- Pada settings.py menambahkan 
``` python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),
]
```
- Menjalankan perintah ```python manage.py collectstatic```

## Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE
- Membuat fungsi baru pada block `<Script>` dengan nama deleteItem(itemId)
```
async function deleteItem(itemId) {
    const deleteUrl = `{% url 'main:delete_item_ajax' item_id=999 %}`.replace('999', itemId);
    console.log(itemId);
    try {
        const response = await fetch(deleteUrl, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        }).then(refreshItems)
        
    } catch (error) {
        console.error('Error:', error);
    }
}
```
- Menambahkan button yang berfungsi untuk menampilkan delete
```<button data-id="${item.pk}" class="btn btn-danger btn-sm button-delete" onclick="deleteItem(this.getAttribute('data-id'))">Delete</button>```
- Membuka `views.py` dan membuat fungsi 'delete_item_ajax' 
``` python
@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=item_id)
        item.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)
```
- Membuka file `urls.py` pada folder `main` dan import fungsi `delete_item_ajax`
- Menambahkan path url kedua fungsi tersebut ke dalam urlpatterns
```path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax')```