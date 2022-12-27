from django.shortcuts import render,redirect
from .forms import Product_form,Review_form
# Create your views here.
def Product_view(request):
    form=Product_form()
    if request.method =='POST' and request.FILES:
        form=Product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/review')
    return render(request,'products.html',{'form':form})

def Review_view(request):
    form=Review_form()
    return render(request,'review.html',{'form':form})