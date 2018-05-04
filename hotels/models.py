from django.db import models



class cities(models.Model):
    cname=models.CharField(max_length=20)

    def __str__(self):
        return self.cname

class accommodation(models.Model):
   # pid = models.ForeignKey(pcks, on_delete=models.CASCADE)
    cid=models.ForeignKey(cities,on_delete=models.CASCADE)
    hname=models.CharField(max_length=100)
    single=models.CharField(max_length=5)
    double=models.CharField(max_length=5)
    family=models.CharField(max_length=5)
    multiple=models.CharField(max_length=5)
    sno=models.IntegerField(default=5)
    dno=models.IntegerField(default=5)
    fno=models.IntegerField(default=5)
    mno=models.IntegerField(default=5)
    img1=models.CharField(max_length=2000,default="/static/hotels/images/20-seater.jpg")
    img2=models.CharField(max_length=2000,default="/static/hotels/images/20-seater.jpg")
    img3=models.CharField(max_length=2000,default="/static/hotels/images/20-seater.jpg")


    def __str__(self):
        return self.hname


#class conveyance(models.Model):
    # vid=models.IntegerField
 #   cid = models.ForeignKey(cities, on_delete=models.CASCADE)
  # count = models.IntegerField(default=10)
    #costperkm = models.CharField(max_length=3)
    #img=models.CharField(max_length=3000,default="/static/hotels/images/20-seater.jpg")

#    def __str__(self):
 #       return self.vehicles

class hbookings(models.Model):
    city = models.CharField(max_length=50)
    hotel_name = models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=12)
    Checkin=models.CharField(max_length=15)
    Checkout = models.CharField(max_length=15)
    email=models.CharField(max_length=25)
    bookintype=models.CharField(max_length=100)
    bookincost=models.IntegerField(default=1500)
    def __str__(self):
        return self.name