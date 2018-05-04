from django.contrib.auth.models import User
from django import forms
from .models import *


class SingleroomForm(forms.ModelForm):
    class Meta:
        model = hbookings
        #fields = ['name','contact','email','start_date']
        exclude = ['bookintype','bookincost','city','hotel_name']

class DoubleroomForm(forms.ModelForm):
    class Meta:
        model = hbookings
        #fields = ['name','contact','email','start_date']
        exclude = ['bookintype','bookincost','city','hotel_name']

class MultipleroomForm(forms.ModelForm):
    class Meta:
        model = hbookings
        #fields = ['name','contact','email','start_date']
        exclude = ['bookintype','bookincost','city','hotel_name']

class FamilyroomForm(forms.ModelForm):
    class Meta:
        model = hbookings
        #fields = ['name','contact','email','start_date']
        exclude = ['bookintype','bookincost','city','hotel_name']