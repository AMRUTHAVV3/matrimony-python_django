from django.db import models

# Create your models here.
class userregistrationdb(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    uemail=models.EmailField(max_length=50,null=True,blank=True)
    upass=models.CharField(max_length=50)
    mobile=models.IntegerField()

class customer_registrationdb(models.Model):
    fname=models.CharField(max_length=50,null=True,blank=True)
    lname=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    dob=models.CharField(max_length=50,null=True,blank=True)
    picture=models.ImageField(upload_to="customer pics",null=True,blank=True)
    caste=models.CharField(max_length=50,null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    qualification=models.CharField(max_length=50,null=True,blank=True)
    occupation=models.CharField(max_length=50,null=True,blank=True)
    workaddress=models.CharField(max_length=50,null=True,blank=True)
    hobby=models.CharField(max_length=50,null=True,blank=True)
    fathername=models.CharField(max_length=50,null=True,blank=True)
    mothername=models.CharField(max_length=50,null=True,blank=True)
    fathercontact=models.IntegerField()
    address=models.CharField(max_length=50,null=True,blank=True)
    # streetnr=models.CharField(max_length=50,null=True,blank=True)
    # zipcode=models.IntegerField(null=True,blank=True)
    # place=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
class sendmessagedb(models.Model):

    user_name=models.CharField(max_length=50,null=True,blank=True)


    fname=models.CharField(max_length=100,null=True,blank=True)
    lname=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)




class feedbackdb(models.Model):

    user=models.CharField(max_length=100,null=True,blank=True)
    # fname=models.CharField(max_length=100, null=True, blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)
