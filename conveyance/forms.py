from django.contrib.auth.models import User
from django import forms
from .models import *

class BookingsForm(forms.ModelForm):
    class Meta:
        model = renting
        #fields = ['name','contact','email','start_date']
        exclude = ['vehicle_name']