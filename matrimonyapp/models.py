from django.db import models

# Create your models here.
class customerdb(models.Model):
    cname=models.CharField(max_length=50)
    cpic=models.ImageField(upload_to='customer pics')
    cno=models.IntegerField(null=True,blank=True)
    emil=models.EmailField(max_length=50)
    dob=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50)
    adrs=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    fcont=models.IntegerField(null=True,blank=True)
    wadrs=models.CharField(max_length=50)
    hoby=models.CharField(max_length=50)
    quali=models.CharField(max_length=50,null=True,blank=True)
    occutn=models.CharField(max_length=50)

    cast=models.CharField(max_length=50)
