from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    if request.method=="GET":
        username=request.GET.get("user")
    return render(request,"index.html",{"username":username})

def sign_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        url = "/?user={}".format(username)
        return HttpResponseRedirect(url)
    return render(request,"signin.html")

def return_ord(request):
    return render(request,"return.html")

def cart(request):
    return render(request,"cart.html")

