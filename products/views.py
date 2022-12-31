from django.shortcuts import render,redirect
from .forms import Product_form,Review_form
from .models import Product,Review
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/cust/login/')
def HomePage(request):
    return render(request,'home.html')




@login_required(login_url='/cust/login/')
def Product_view(request):
    form=Product_form()
    if request.method =='POST' and request.FILES:
        form=Product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/proread')
    return render(request,'products.html',{'form':form})

@login_required(login_url='/cust/login/')
def Review_view(request):
    form=Review_form()
    if request.method =='POST':
        form=Review_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/proread')

    return render(request,'review.html',{'form':form})

@login_required(login_url='/cust/login/')
def ProductRead(request):
    obj=Product.objects.all()
    obj2=Review.objects.all()
    return render(request,'proread.html',{'pobj':obj,'robj':obj2})


@login_required(login_url='/cust/login/')
def ReviewRead(request,pk):
    obj=Review.objects.filter(product_id=pk)
    return render(request,'proread.html',{'robj':obj})

@login_required(login_url='/cust/login/')
def ProductUpdate(request,pk):
    obj=Product.objects.get(id=pk)
    form=Product_form(instance=obj)
    if request.method =='POST'  and request.FILES:
        form=Product_form(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/proread')
    return render(request,'proupdate.html',{'form':form,'obj':obj.product_image})