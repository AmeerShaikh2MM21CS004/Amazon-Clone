from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import userForm
from amazon_service_footer.models import Service
from amazon_footer_data.models import Footer_Block
from user_contact.models import UseerDetails

def home(request):
    serviceData=Service.objects.all()
    footer_service=Footer_Block.objects.all()

    if request.method=="GET":
         username=request.GET.get("user")
    return render(request,"index.html",{"username":username,"servicedata":serviceData,'footer_block':footer_service})

def sign_in(request):

    # if request.method=="POST":
    #     username=request.POST.get("username")
    #     password=request.POST.get("password")

    #     url='/?user={}'.format(username)
    
    #     return HttpResponseRedirect(url)
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')

        # user_data=UseerDetails(username='username',password='password')
        # user_data.save()

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
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_detail=UseerDetails(username=username,password=password)
            user_detail.save()

            url='/?user={}'.format(username)
    
            return HttpResponseRedirect(url)

     

