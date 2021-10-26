from django.shortcuts import render
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    """ A view to return the index page """
    try:
        products = Product.objects.all()
        home_pre_orders = Product.objects.filter(category__name='pre_orders_funk_soul_jazz')
        merchandise = Product.objects.filter(category__name='slip_mats')
    except ObjectDoesNotExist:
        products = None


    context = {
        'products': products,
        'home_pre_orders': home_pre_orders,
        'merchandise': merchandise,
    }
    return render(request, 'home/index.html', context)
