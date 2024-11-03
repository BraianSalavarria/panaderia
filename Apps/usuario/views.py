from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        user = authenticate(request,username=username,password=password)
        if user:
                login(request,user)
                return redirect(reverse('home'))
        else:
                messages.error(request,'error en credenciales')
                return render(request,'usuario/login.html')  

    return render(request,'usuario/login.html') 


def logout_view(request):
    logout(request)
    messages.success(request,'Usuario deslogeado')
    return redirect(to='usuario:login')

