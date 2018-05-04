
from django.db import models

# Create your models here.
class userinfo(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    phone=models.CharField(max_length=11)
    mail=models.CharField(max_length=25)