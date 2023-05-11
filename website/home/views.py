from django.shortcuts import render, redirect, get_object_or_404
from .forms import loginform, signUpForm
from django.views import View, generic
from .models import product, cart, fileupload, orders
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

def cart(request, pk):
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
    carts = product.objects.get(id = pk)
    # cartd = cart(request)
    if request.method == 'POST':
        image = item['ImageField']
        name = item['name']
        price = item['price']
        number = item['number']
        cartd = cart.objects.create(ImageField, name, price, number)
        cartd.save()
    carts.save()
    # cart = cart(request)
    

    # def map_function(p):
    #     pid = str(p.id)
    #     q = cart.cart[pid]['quantity']
    #     return {'product': p, 'quantity': q, 'total': p.price*q, 'form': CartForm(initial={'quantity': q, 'product_id': pid})}

    # cart_items = map(map_function, product)
    # return render(request, 'cart/cart_details.html', {'cart_items': cart_items, 'total': cart.get_total_price()})

    # if request.method == 'POST':
    #    form = cart(request.POST)
    #    if form.is_valid():
    #         form.save()
     # Lấy sản phẩm dựa trên id
    # productd = get_object_or_404(product,id = pk)
    # Lấy giỏ hàng hiện tại của người dùng hoặc tạo một giỏ hàng mới nếu người dùng chưa có giỏ hàng
    # if request.method == 'POST':
    #     carts = cart(request.POST)
    #     if carts.is_valid():
        # Thêm sản phẩm vào giỏ hàng
            # carts.add(cart=productd)
            # def add(product):
            #     product_id = str(product.id)
            #     if product_id not in carts:
            #         cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            #         cart[product_id]['quantity'] += 1
            #         carts.save()
        # Chuyển hướng đến trang giỏ hàng
    return render(request, 'home/cart.html', {'carts':carts})
            # return redirect('home')
# def clear():
#         # Xóa giỏ hàng khỏi session
#     del session[settings.CART_SESSION_ID]
#     session.modified = True
    # try:
    #     carts = cart.objects.get(user = request.user, product = product)
    #     carts.quantity +=1
    #     carts.save()
    # except cart.DoesNotExist:
    #     cart = cart.objects.create(user = request.user, product = product)
    # return render(request, 'home/cart.html')
# def product_detail(request, name):
#     model = product
#     queryset = product.objects.all()
#     context_name = 'products'
#     qs = super().get_queryset()
#     if 'category' in kw
#     return render(request, 'home/product.html', {'product':product})
# def remove_from_cart(request, pk):
#     productd = cart.objects.all()
#     cart = cart(request)
#     cartd = cart.objects.get(id = pk)
#     cart.remove(cartd)
#     return redirect('cart')
#     return render(request, 'home/cart.html', {'productd':productd})
def search(request):
    query = request.GET.get('query')
    # query = form.cleaned_data.get('query', '')
    results = []
    if query:
        # Sử dụng Q objects và icontains để tìm kiếm sản phẩm
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    context = {
        # 'form': form,
        'query': query,
        'results': results
    }
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = None
    return render(request, 'home/search.html', {'results': results})
def remove_from_cart(request, pk):
    cart = cart(request)
    cart.remove(str(pk))
    return redirect('cart')
def out(request):
    if request.method == 'POST':
        username = request.POST['username'] # truyền thông tin theo phương thức post
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email ,password)
        user.save()
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/signup.html')
    return render(request, "home/checkout.html")
def orders(request, pk):
    order = product.objects.get(id=pk)
    return render(request, 'home/order.html', {'order':order})
    if request.method == 'POST':
        name = request.POST['name'] # truyền thông tin theo phương thức post
        email = request.POST['email']
        adsresss = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        user = User.objects.create_user(username, email ,password)
        user.save()
        
        return render(request, 'home/order.html', {'order':order})
    else:
        return render(request, 'home/index.html')
    return render(request, "home/order.html")