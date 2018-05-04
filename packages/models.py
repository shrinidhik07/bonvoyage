
from django.db import models
from django.core.urlresolvers import reverse


class pcks(models.Model):
    #pid=models.IntegerField
    pname=models.CharField(max_length=200)
    places=models.CharField(max_length=250)
    price=models.CharField(max_length=10)
    duration=models.CharField(max_length=10)
    img=models.CharField(max_length=3000)
    i1= models.CharField(max_length=2000,default="/static/packages/images/a1.jpg")
    i2= models.CharField(max_length=2000,default="/static/packages/images/a1.jpg")
    i3= models.CharField(max_length=2000,default="/static/packages/images/a1.jpg")
    i4= models.CharField(max_length=2000,default="/static/packages/images/a1.jpg")
    def __str__(self):
        return self.pname

class cityinfo(models.Model):
    pid=models.ForeignKey(pcks,on_delete=models.CASCADE)
    attractions=models.CharField(max_length=500)
    guide=models.CharField(max_length=50)


    def __str__(self):
        return self.attractions

class bookings(models.Model):
    package_name=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=12)
    start_date=models.CharField(max_length=15)
    email=models.CharField(max_length=25)


    def __str__(self):
        return self.name

