from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def CustomerView(request):
    form=CustomerForm()
    if request.method == 'POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            subject = f'Hi {username} welcome to Digicart'
            message= f'Thank you for registering to Digicart and your username is {username} and password is {password}'
            recipient_list=[form.cleaned_data['email']]
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject,message,from_email,recipient_list)
            return HttpResponse('user is created')


    return render(request,'custpage.html',{'form':form})

def CustomerLogin(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'hi {username} you successfully login to the application')
                return redirect('/home/')
    return render(request,'custlogin.html',{'form':form})

@login_required(login_url='/cust/login/')
def CustomerLogout(request):
    logout(request)
    messages.success(request,'hi u successfully logedout')
    return redirect('/cust/login/')