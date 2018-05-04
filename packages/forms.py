from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']



class BookingsForm(forms.ModelForm):
    class Meta:
        model = bookings
        #fields = ['name','contact','email','start_date']
        exclude = ['package_name']