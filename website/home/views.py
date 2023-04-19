from django.shortcuts import render
# from django.views import View
# from .forms import loginform
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# Create your views here.
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
def login(request):
    return render(request, 'home/login.html')
def logup(request):
    return render(request, 'home/signup.html')
def shop(request):
    return render(request, 'home/shop.html')
def single(request):
    return render(request, 'home/shop-single.html')
def cart(request):
    return render(request, 'home/cart.html')