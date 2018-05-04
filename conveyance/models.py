from django.db import models

# Create your models here.

class cities(models.Model):
    cname=models.CharField(max_length=20)

    def __str__(self):
        return self.cname
class vehicles(models.Model):
    # vid=models.IntegerField
    cid = models.ForeignKey(cities, on_delete=models.CASCADE)
    vname = models.CharField(max_length=100)
    hours = models.IntegerField(default=12)
    count = models.IntegerField(default=10)
    costperkm = models.CharField(max_length=6)
    img=models.CharField(max_length=3000,default="/static/conveyance/images/x8.jpg")

    def __str__(self):
        return self.vname


class renting(models.Model):
    vehicle_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=12)
    email=models.CharField(max_length=25)
    starttime=models.CharField(max_length=6)

    def __str__(self):
        return self.name