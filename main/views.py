from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'nama_aplikasi': 'Pacil Library',
        'nama': "Nabila Zavira",
        'kelas': "PBP D", 
    }

    return render(request, "main.html", context)