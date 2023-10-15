from django.db import models
from django.contrib.auth.models import User

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
    gender=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.user_name


# class receivemsgdb(models.Model):
#     user_name=models.ForeignKey(sendmessagedb,null=True,on_delete=models.CASCADE)
#     # fname=models.ForeignKey(sendmessagedb,null=True,on_delete=models.CASCADE,related_name="receivemsg")
#     # message=models.ForeignKey(sendmessagedb,null=True,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user_name







class feedbackdb(models.Model):

    user=models.CharField(max_length=100,null=True,blank=True)
    # fname=models.CharField(max_length=100, null=True, blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)
class contactdb(models.Model):
    msg=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)


class successstorydb(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    pname=models.CharField(max_length=100,null=True,blank=True)
    c_image=models.ImageField(upload_to="successstory_photo",null=True,blank=True)
    story = models.CharField(max_length=100, null=True, blank=True)

class verificationdb(models.Model):

    sender=models.CharField(max_length=100, null=True, blank=True)
    reciever=models.CharField(max_length=100, null=True, blank=True)
    status=models.CharField(max_length=100, null=True, blank=True)
