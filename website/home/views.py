from django.shortcuts import render, redirect
from .forms import loginform, signUpForm
from django.views import View
from .models import product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request, 'home/index.html')
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
    return render(request, 'home/shop.html')
def single(request):
    return render(request, 'home/shop-single.html')
def cart(request):
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
    return render(request, 'home/cart.html')