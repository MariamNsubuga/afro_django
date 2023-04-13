from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    pr_title = "Afro Django"  # variable to used in index file
    username = 'Mariam'
    gender = 'Female'
    return render(request,
                  'index.html',
                  {'pr_title':pr_title, 'username':username, 'gender': gender})

# register view
def register(request):
    return render(request, 'register.html')

def registration(request):
   username = request.POST['username']
   password = request.POST['password']
   email = request.POST['email']
   gender = request.POST['gender']
   user_details = [username , email, password, gender]
   print (user_details)
   return render(request, 'index.html',{'username':username})
    
  
