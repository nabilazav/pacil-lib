from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Harry Potter',
        'amount': "7",
        'description': "Novels", 
    }

    return render(request, "main.html", context)