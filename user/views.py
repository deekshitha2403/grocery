from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

def register_user(request):
  if request.method=="POST":
    uname = request.POST["user_name"]
    eml = request.POST["user_email"]
    password_one = request.POST["password_one"]
    password_two = request.POST["password_two"]
    
    if password_one == password_two:
      if User.objects.filter(username=uname).exists():
        messages.warning(request, f"The username `{uname}` is already taken, please give alternative ")
        return redirect("/user/register-user/")
      else:
         User.objects.create_user(username=uname, email=eml, password=password_one)
         messages.success(request, f"User created successfully for {uname}") 
         return redirect("/user/login-user/")
    else:
      messages.warning(request, "password and confirm password not matched") 
      return redirect("register-user/")
  return render(request, 'user/register_user.html')

def login_user(request):
  if request.method=='POST':
    uname = request.POST["user_name"]
    pswd = request.POST["password_one"]
    user = authenticate(username=uname, password=pswd)
    if user is not None:
      login(request,user)
      return redirect("/")
  return render(request,'user/login_user.html')

def logout_user(request):
  logout(request)
  return redirect("/")