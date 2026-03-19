from django.shortcuts import render,redirect,get_object_or_404

from .forms import SearchForm
from .models import Product, Category,Cart


def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    X = {
        'Name' : 'PAVI',
        'Age' : 23,
        'Place' : 'Chennai'
    }
    return render(request,'about.html',X)
def products(request):
    categories = Category.objects.all()
    data = []
    for cat in categories:
        products = Product.objects.filter(category = cat)
        data.append({
            'category' : cat,
            'products' : products
        })
        context = {
            'data' : data,
        }
    return render(request,'products.html',context)
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    Cart.objects.create(
        product=product
    )
    return redirect('cart')
def cart(request):
    cart_items = Cart.objects.all()
    return render(request,'cart.html',{'cart_items':cart_items})
def payment_method(request,id):
    product = Product.objects.get(id = id)
    return render(request, 'payment_method.html',{'product':product})
def search(request):
    form=SearchForm()
    return render(request,'search.html',{'form':form})
def contact(request):
       return render(request,'contact.html')