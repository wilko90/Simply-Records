from django.shortcuts import render
from products.models import Product, Category
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    try:
        products = Product.objects.all()
        home_pre_orders = Product.objects.filter(category__name='pre_orders_funk_soul_jazz')
        equipment = Product.objects.filter(category__name='equipment_products')
        merchandise = Product.objects.filter(category__name='merchandise_products')
    except ObjectDoesNotExist:
        products = None
        categories = None


    context = {
        'products': products,
        'home_pre_orders': home_pre_orders,
        'equipment': equipment,
        'merchandise': merchandise,
    }
    return render(request, 'home/index.html', context)
