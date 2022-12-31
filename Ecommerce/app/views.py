# from itertools import product
# from statistics import quantiles
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
# from .forms import CustomerRegistrationForm, CustomerProfileForm
# from django.contrib import messages
# from django.db.models import Q
# from django.http import JsonResponse
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.models import User




# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears= Product.objects.filter(category='BW')
        mobiles= Product.objects.filter(category='M')
        laptops= Product.objects.filter(category='L')
        return render(request, 'app/home.html',{'bottomwears':bottomwears,'topwears':topwears,'mobiles':mobiles,'laptops':laptops})

def product_detail(request):
    return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            return render(request, 'app/productdetail.html',{'product':product, 'item_already_in_cart':item_already_in_cart})
        else:
            return render(request, 'app/productdetail.html',{'product':product, 'item_already_in_cart':item_already_in_cart})

# def add_to_cart(request):
#  return render(request, 'app/addtocart.html')

# @login_required
# def add_to_cart(request):
#     user = request.user
#     product_id =request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user, product=product).save()
#     return redirect('/cart')


def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')