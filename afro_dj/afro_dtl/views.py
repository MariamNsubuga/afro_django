from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User_account
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    pr_title = "Afro Django"  # variable to used in index file
    
    if request.user.is_authenticated:
        username = request.user.username
        
        return render(request,
                  'index.html',
                  {'pr_title':pr_title, 'username':username})
    else:
         author = 'Mariam'
         gender = 'Female'
         return render(request,
                  'index.html',
                  {'pr_title':pr_title, 'author':author, 'gender': gender})

   
# register view
def register(request):
    return render(request, 'register.html')

def registration(request):
   user_name = request.POST['username']
   password = request.POST['password']
   email = request.POST['user_email']
   gender = request.POST['gender']
   user_details = [user_name , email, password, gender]
   print (user_details)
   if User.objects.filter(username=user_name).first():
       print ('Username already exists')
       return render(request, 'login.html')
   else:
       user = User.objects.create_user(user_name, email, password)
       return render(request, 'login.html')
#    return render(request, 'index.html',{'username':user_name})

def login_user(request):
    user_name = request.POST['username']
    pwd = request.POST['password'] 
    if User.objects.filter(username=user_name):
        print('This username exists')
        logged_user = authenticate(request, username=user_name, password=pwd)
        if logged_user is not None:
            #here we are logging in the user
            auth_login(request, logged_user)
            print(user_name + " "+"Logged in successfuly")
            return redirect('index')
        else:
            #we handle a scenario where the authentication has failed
            return render(request, 'login.html')
    else:
        print('user credentials do not exit')
        return render(request, 'login.html')
    
def login_page(request):
    return render(request, 'login.html')

@login_required
def logout_user(request):
    auth_logout(request)
    return redirect ('login_page')
