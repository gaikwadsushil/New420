from django.forms import ModelForm
from .models import Brand,Product


class BrandCreationFrom(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
    field_order = ['name',
                   'logo',
                   'origin',
                   'tagline',
                   'types',
                   'since',] 


class ProductCreationFrom(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    field_order = ['name','slug','price_inclusive',
                  'description','brand','gst_rate',
                  'hsn_code','quantity','features',]
    