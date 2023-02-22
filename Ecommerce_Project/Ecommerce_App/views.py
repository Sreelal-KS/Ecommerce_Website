from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def allProductsCategory(request, c_slug=None):
    category_page = None
    products_list = None
    if c_slug != None:  # any category in slug url
        category_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=category_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', 1))  # 'page' means total number of pages and '1' is the default page value
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "category.html", {'category': category_page, 'product': products})


def productDetails(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, "products.html", {'product': product})
