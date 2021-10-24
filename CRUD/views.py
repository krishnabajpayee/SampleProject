from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
import random
import string

# Create your views here.

def Index(request):
    msg=''
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        data=User.objects.get(email=email)
        user=authenticate(username=data,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/profile/')
        msg="Sorry Invalid Request"
    return render(request, 'login.html', {'msg':msg})

def RegisterUser(request):
    CHAR=string.digits
    if request.method=="POST":
        firstName=request.POST.get("firstname")
        lastName=request.POST.get("lastname")
        email=request.POST.get("email")
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        try:
            chekUsername=User.objects.get(username=firstName)
            username="".join(random.choice(firstName+CHAR) for i in range(8))
        except:
                username=firstName
        if password1 != password2:
            msg="Password Should be same"
            return render(request, 'register.html',{'msg':msg})
        
        User.objects.create_user(username=username,first_name=firstName,last_name=lastName,email=email,password=password2)
        
        return redirect("/")
    return render(request, 'register.html')

def Profile(request):
    return render(request,'profile.html')

def EditUser(request):
    return render(request,'editUser.html')
