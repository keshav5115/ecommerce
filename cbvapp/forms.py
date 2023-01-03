from django import forms
from .models import Orders


class ordersform(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['product','customer','quantity']