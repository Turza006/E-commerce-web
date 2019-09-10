from django.shortcuts import render



def home(request):
    return render(request,'products/products_home.html')


