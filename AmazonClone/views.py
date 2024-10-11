from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import userForm
from amazon_service_footer.models import Service

def home(request):
    serviceData=Service.objects.all()
    
    if request.method=="GET":
         username=request.GET.get("user")
    return render(request,"index.html",{"username":username,"servicedata":serviceData})

def sign_in(request):

    # if request.method=="POST":
    #     username=request.POST.get("username")
    #     password=request.POST.get("password")

    #     url='/?user={}'.format(username)
    
    #     return HttpResponseRedirect(url)
    return render(request,"signin.html")

def return_ord(request):
    return render(request,"return.html")

def cart(request):
    return render(request,"cart.html")

def user_data(request):
     if request.method=="POST":
        if request.POST.get("username")=="":
            return render(request,"signin.html",{"error":True})
        else:
            username=request.POST.get("username")
            password=request.POST.get("password")

            url='/?user={}'.format(username)
    
            return HttpResponseRedirect(url)

     

