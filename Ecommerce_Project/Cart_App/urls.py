from django.urls import path
from . import views

app_name = 'Cart_App'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='Cart_Remove'),
    path('cart_delete/<int:product_id>/', views.cart_delete, name='Cart_Delete'),
]
