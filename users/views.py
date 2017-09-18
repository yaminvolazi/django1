# -*- coding: utf-8 -*-
from django.shortcuts import render
from .form import UserForm
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

title = "VOLAZI Users Management System - VUMS"

######################################### home

def home(request):
    user_name = "sign in - register"
    if request.user.is_authenticated():
        user_name="Welcome : %s" %(request.user)

    form = UserForm(request.POST or None)
    context = {
        "template_title": title,
        "template_user_name": user_name,
        "form": form
    }

    form=UserForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        data = list(User.objects.all())

        context ={
            "template_title":title,
            "template_user_name":user_name,
            "template_data":data
        }
        return render(request, "dashboard.html", context)

    return render(request,"home.html",context)

######################################### dashboard

def dashboard(request):
    user_name = "sign in - register"
    if request.user.is_authenticated():
        user_name="Welcome : %s" %(request.user)
    data = list(User.objects.all())

    context = {
        "template_title": title,
        "template_user_name": user_name,
        "template_data": data
    }

    return render(request, "dashboard.html", context)

######################################### update

def update(request,pk):
    user_name = "sign in - register"
    if request.user.is_authenticated():
        user_name="Welcome : %s" %(request.user)

    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None,initial={'first_name': user.first_name,'last_name': user.last_name,'telephone': user.telephone,'email':user.email})
    context = {
        "template_title": title,
        "template_user_name": user_name,
        "form": form,
    }

    form=UserForm(request.POST or None)

    if form.is_valid():
        user = get_object_or_404(User, pk=pk)
        #user = User.objects.get(first_name="test")

        user.first_name=form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.telephone = form.cleaned_data.get('telephone')
        user.email = form.cleaned_data.get('email')

        user.save()
        #instance = form.save()
        data = list(User.objects.all())

        context ={
            "template_title":title,
            "template_user_name":user_name,
            "template_data":data
        }
        return render(request, "dashboard.html", context)

    return render(request,"update_user.html",context)

######################################### delete

def delete(request,pk):
    user_name = "sign in - register"
    if request.user.is_authenticated():
        user_name="Welcome : %s" %(request.user)

    user = get_object_or_404(User, pk=pk)

    #user = User.objects.get(first_name="test")
    #user.delete()

    context = {
        "template_title": title,
        "template_user_name": user_name,
        "template_user": user
    }

    if request.method == 'POST':
        user.delete()
        data = list(User.objects.all())
        context = {
            "template_title": title,
            "template_user_name": user_name,
            "template_data": data,
            "template_user": user
        }
        return render(request, "dashboard.html", context)

    return render(request, "delete_user.html", context)