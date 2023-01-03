from django.shortcuts import render
from django.http import HttpResponse
from .forms import ordersform
from django.views import View
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from .models import Orders
# Create your views here.

#---------func based view--------------------
def orderview(request):
    form=ordersform()
    if request.method=='POST':
        form=ordersform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('your order has been placed')
    return render(request,'order.html',{'form':form})


def orderupdate(request,pk):
    obj=Orders.objects.get(orderid=pk)
    form = ordersform(instance=obj)
    if request.method == 'POST':
        form= ordersform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('order has been updated')

    return render(request,'orderupdate.html',{'form':form})

#---------class based views------------------
class Cbvorderview(View):
    def get(self,request):
        form=ordersform()
        return render(request,'order.html',{'form':form})

    def post(self,request):
        
        form=ordersform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('your order has been placed')


class Cbvorderupdate(View):
    def get(self,request,pk):
        obj=Orders.objects.get(orderid=pk)
        form = ordersform(instance=obj)
        return render(request,'orderupdate.html',{'form':form})
    
    def post(self,request,pk):
        obj=Orders.objects.get(orderid=pk)
        form = ordersform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('order has been updated')

class Cbvorderread(View):
    def get(self,request):
        obj=Orders.objects.all()
        
        return render(request,'orderread.html',{'obj':obj})