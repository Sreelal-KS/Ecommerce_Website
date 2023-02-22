from django.shortcuts import render
from Ecommerce_App.models import Category, Product
from django.db.models import Q  # For Query related operations


# Create your views here.

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
