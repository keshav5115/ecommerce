from django import forms
from .models import Customer
from django.contrib.auth.hashers import make_password
class CustomerForm(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Customer
        fields=['username','first_name','last_name','email','mobile','gender','password','password2']

    def save(self,commit=True):
        user=super().save(commit=False)
        password=user.password
        password2=self.cleaned_data['password2']
        if password == password2:
           encpassword = make_password(password)
           user.password=encpassword
           if commit:
                user.save()
                return user
            

