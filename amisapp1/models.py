from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userType_table(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userType = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True,blank=True);
    bloodgroup = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    postal = models.IntegerField(null=True,blank=True)
    about = models.CharField(max_length=500,null=True,blank=True)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.first_name

class patientBookAppointment(models.Model):
    name = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    problems = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

class queryForm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
