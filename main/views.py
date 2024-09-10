from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Amesoup',
        'user_name': 'Muhammad Afwan Hafizh',
        'class_name': 'PBP-F'
    }

    return render(request, "main.html", context)

def account_page(request):
    context = {
        'app_name': 'Amesoup',
        'user_name': 'Muhammad Afwan Hafizh',
        'class_name': 'PBP-F'
    }
    return render(request, 'account.html', context)

def products_page(request):
    return render(request, 'products.html')

def cart_page(request):
    return render(request, 'cart.html')