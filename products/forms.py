from django import forms
from .models import Product,Review

class Product_form(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        

class Review_form(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        widgets={'rating':forms.RadioSelect()}