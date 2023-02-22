from . import views
from django.urls import path

app_name = 'Ecommerce_App'
urlpatterns = [
    path('', views.allProductsCategory, name='AllProductsCategory'),
    path('<slug:c_slug>/', views.allProductsCategory, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.productDetails, name='product_details')
]
