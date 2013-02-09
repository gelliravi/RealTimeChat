# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login(request):
  errors = []
  if request.user.is_authenticated():
    HttpResponseRedirect("/accounts/profile/")
  singin_form = SigninForm()
  if request.method == "POST":
    singin_form = SigninForm(request.POST)
    if singin_form.is_valid():
        user = authenticate(username=request.POST['login'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            if request.GET['next'] is not None:
                HttpResponseRedirect(request.GET['next'])
            else:
                HttpResponseRedirect('/accounts/profile/')
        else:
            errors.append('Не верный логин или пароль')
  return render_to_response("accounts/login.html",{'form' : singin_form,'errors':errors})    

@login_required
def profile(request):
  user = request.user.get_full_name
  return render_to_response("accounts/index.html",{'user':user})

def singup(request):
  if request.user.is_authenticated():
    HttpResponseRedirect("/accounts/profile/")  
  errors = []  
  form = SingupForm()  
  if request.method == "POST":
    form = SingupForm(request.POST)
    if form.is_valid():
      try:
        user = User.objects.get(username=request.POST['login'])
        errors.append('Кто-то под таким именем уже существует')
      except User.DoesNotExist:
        try:
            user = User.objects.get(email=request.POST['email'])
            errors.append('Данный email уже есть в базе')
        except User.DoesNotExist:    
            user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['password'])
  return render_to_response("accounts/singup.html",{'form': form,'errors':errors})

@login_required
def logout(request):
    logout(request)