from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Amesoup',
        'user_name': 'Muhammad Afwan Hafizh',
        'class_name': 'PBP-F'
    }

    return render(request, "main.html", context)