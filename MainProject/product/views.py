from django.shortcuts import render,redirect
from .models import Brand
from django.views import View
from .models import Product
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
        