from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256444',
        'name': 'Muhammad Brian Subekti',
        'class': 'PBPKKI'
    }

    return render(request, "main.html", context)