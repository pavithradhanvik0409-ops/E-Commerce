from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('home', views.home,name = 'home'),
    path('about', views.about,name = 'about'),
    path('product',views.products,name = 'products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart,name = 'add_to_cart'),
    path('cart',views.cart,name = 'cart'),
    path('payment/<int:id>/', views.payment_method,name = 'payment_method'),
    path('search',views.search,name = 'search'),
    path('contact',views.contact,name = 'contact'),
]

















# path('payment',views.payment,name = 'payment_method'),