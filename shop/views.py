from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from django.contrib import messages


def allproducts(request, slug_cat=None):
     page_cat = None
     products = None
     if slug_cat != None:
          page_cat=get_object_or_404(Category, slug=slug_cat)
          products=Product.objects.all().filter(category=page_cat, available=True)
     else:
          products = Product.objects.all().filter(available=True)
     return render(request,'home.html',{'category': page_cat, 'products': products})




# Create your views here.
def cat_prod(request,slug_cat=None, slug_prod=None):
     try:
          product = Product.objects.get(category__slug=slug_cat, slug=slug_prod)
     except Exception as e:
          raise e
     return render(request, 'product.html',{'product':product})


def signup(request):
     if request.method == 'POST':
          username=request.POST['username']
          fname=request.POST['fname']
          lname=request.POST['lname']
          email=request.POST['email']
          password1=request.POST['password1']
          password2=request.POST['password2']


          myuser = User.objects.create_user(username, email, password1)
          myuser.first_name=fname
          myuser.last_name=lname

          myuser.save()
          return redirect('signin')
     return render(request, 'signup.html')

def signin(request):
     if request.method=="POST":
          username=request.POST['username']
          password1=request.POST['password1']

          user = authenticate(username=username, password=password1)

          if user is not None:
               login(request, user)
               fname=user.first_name
               return render(request, 'user_profile.html', {'fname': fname})
          else:
               messages.error(request, "Invalid Credentials")
               return redirect('home')



     return render(request, 'signin.html')


def signout(request):
     logout(request)
     return redirect('allproducts')
