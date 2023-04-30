from django.shortcuts import render, redirect, get_object_or_404
from .forms import loginform, signUpForm
from django.views import View, generic
from .models import product, cart, fileupload
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def home(request):
    products = product.objects.all()
    return render(request, 'home/index.html', {'products':products})
# class loginform(View):
#     def login(self, request):
#         cF = loginform
#         return render(request, 'home/login.html', {'cF':cF})
#     def post(self, request):
#         user = request.POST['username']
#         password = request.POST['password']
#         if(user is not None):
#             login(request, user)
#             return render(request, 'home/login.html')
#         else:
#             return render(request, 'home/index.html')

def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html')
            if is_superuser == 1:
                return render(request, 'http://127.0.0.1:8000/admin/')
            else:
                return render(request, 'home/index.html')
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'home/login.html', {'error_message': error_message})
    else:
        success_message = 'Đăng nhập thành công'
        return render(request, 'home/login.html', {'success_message': success_message})

def post(request):
    # return render(request, 'home/signup.html')
    if request.method == 'POST':
        username = request.POST['username'] # truyền thông tin theo phương thức post
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email ,password)
        user.save()
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/signup.html')
def shop(request):
    products = product.objects.all()
    return render(request, 'home/shop.html', {'products':products})
def single(request, pk):
    produc = product.objects.get(id = pk)
    
    return render(request, 'home/shop-single.html', {'produc':produc})

def cart(request, product_id):
    # product = product.objects.get(id = product_id)
    # cart = request.sessions.get('cart', {})
    # cart[product_id] = {
    #     'id': product_id,
    #     'name': product.name,
    #     'price': str(product.price),
    #     'quantity': 1,
    #     'image': product.image.url
    # }
    # request.sessions['cart'] = cart
    product = product.objects.get(id = product_id)
    try:
        cart = cart.objects.get(user = request.user, product = product)
        cart.quantity +=1
        cart.save()
    except cart.DoesNotExist:
        cart = cart.objects.create(user = request.user, product = product)
    return render(request, 'home/cart.html')
# def product_detail(request, name):
#     model = product
#     queryset = product.objects.all()
#     context_name = 'products'
#     qs = super().get_queryset()
#     if 'category' in kw
#     return render(request, 'home/product.html', {'product':product})