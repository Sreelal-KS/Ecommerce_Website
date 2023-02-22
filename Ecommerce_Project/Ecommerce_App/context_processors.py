from .models import Category
from .models import Product


def menu_links(request):
    links = Category.objects.all()
    product_links = Product.objects.all()
    return dict(links=links, p_links=product_links)  # Converting return value into dictionary
