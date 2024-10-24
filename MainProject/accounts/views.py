from django.shortcuts import render,redirect
from  django.contrib.auth.models import User
from django.views import View

# Create your views here.


def register(request):
    if request.method == 'GET':
        print('we are running with GET method')
    
        context = {
        'page_name' : 'Register'
        }
        return render(request,'accounts/register.html',context)

    elif request.method == 'POST':
        print('POST request')
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = User.objects.create_superuser(username=username,password=password)
        print(user.__dict__)
        
        return redirect('/')
    
class Register(View):
    def get(self,request):
        print('GET method')
        context={
            'page_name' : 'Register'
        }
        return render(request,'accounts/register.html',context)
    
    def  post(self,request):
          print('POST request')
          username = request.POST.get('Username')
          password = request.POST.get('password')
          user = User.objects.create_superuser(username=username,password=password)
          print(user)
          
          return redirect('/')
    


def login(request):
    context = {
        'page_name' : 'Log in'
    }
    return render(request,'accounts/login.html',context)