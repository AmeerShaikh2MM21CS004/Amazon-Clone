from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def sign_in(request):
    return render(request,"signin.html")

def return_ord(request):
    return render(request,"return.html")

def cart(request):
    return render(request,"cart.html")