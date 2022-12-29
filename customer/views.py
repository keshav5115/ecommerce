from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
# Create your views here.
def CustomerView(request):
    form=CustomerForm()
    if request.method == 'POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('user is created')


    return render(request,'custpage.html',{'form':form})