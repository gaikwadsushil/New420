from django.shortcuts import render,redirect,get_object_or_404
from .models import Brand,category
from django.views import View
from .models import Product
from .models import Product,ProductImages
from .forms import BrandCreationFrom,ProductCreationFrom
# Create your views here.
def brand_list(request):
    data= Brand.objects.all()
    context ={
        'brands' : data
    }
    return render(request,'product/brand_list.html',context)

class AddProduct(View):
    def get(self, request):
        brands = Brand.objects.all()
        context = {
            'brands': brands
        }
        return render(request,'product/create_product.html',context)
    def post(self,request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        
        Product.objects.create(
            name=name,
            price_inclusive = price,
            description = description,
            brand = Brand.objects.get(name= brand),
            features=''
            )
        return redirect('/')
    
def product_list(request):
    data= Product.objects.all()
    categories = category.objects.all()
    context ={
        'products' : data,
        'categories':categories,
    }
    return render(request,'product/shop.html',context)    


def product_details(request,id): 
     product = get_object_or_404(Product,id = id)
     images = ProductImages.objects.filter(product = product)  
     
     context = {
        'product': product,
        'images': images

    }
     return render(request,'product/product_details.html',context)

def update_product(request,id):
    product = get_object_or_404(Product,id = id)
    brands=Brand.objects.all()
    if request.method == 'GET':
        context = {
         'product': product,
         'brands':brands
     }
     
        return render(request,'product/update_product.html',context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        product.name =name
        product.price_inclusive = price
        product.description = description
        product.brand = Brand.objects.get(name= brand)
        product.save()
        return redirect( 'product_list' )

def add_brand(request):
    brand_from = BrandCreationFrom()
    context={
        'from':brand_from
    }
    return render(request,'product/add_brand.html',context)

def add_product_with_django_from(request):
    product_from = ProductCreationFrom()
    context={
        'from':product_from
    }
    return render(request,'product/create_product.html',context)
        