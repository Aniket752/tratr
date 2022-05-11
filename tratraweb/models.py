from django.db import models

# Create your models here.

class donation(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    orderid=models.IntegerField(default=1)
    Contact=models.IntegerField()
    address=models.CharField(max_length=200)
    amount=models.IntegerField()
    # Pan_no=models.CharField(max_length=20,default="PAN")
    # who=models.CharField(max_length=50)
    # massage=models.CharField(max_length=200)
    def __str__(self):
        return self.Name

class volunteer(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.Name
