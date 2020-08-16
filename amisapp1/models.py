from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class userType_table(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userType = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    age = models.CharField(max_length=20, null=True,blank=True);
    bloodgroup = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    postal = models.CharField(max_length=20, null=True,blank=True)
    about = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10,null=True)
    profile_pic = models.ImageField(upload_to="userProfile",null=True)
    def __str__(self):
        return self.user.first_name

class patientBookAppointment(models.Model):
    name = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    problems = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    date = models.DateField(default=datetime.now().strftime("%dd.%mm.%yyyy"))
    massage = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100)
    address = models.CharField(max_length=100 ,null=True)
    email = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=10,null=True,default=0)
    def __str__(self):
        return self.name


class queryForm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.name
class doctor_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=20,null=True)
    about = models.CharField(max_length=500,null=True)
    clinicInfo = models.CharField(max_length=100,null=True)
    clinicAddress = models.CharField(max_length=100,null=True)
    address1 =  models.CharField(max_length=200,null=True)
    address2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True)
    pin = models.CharField(max_length=20, null=True)
    service = models.CharField(max_length=200,null=True)
    specialization = models.CharField(max_length=200,null=True)
    profile_pic  = models.ImageField(upload_to="doctorProfile",null=True)
    
    def __str__(self):
        return self.user.first_name


class dawa_category(models.Model):
    user = models.CharField(max_length=50,null=True)
    category = models.CharField(max_length=100)
    added_on = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.category

class dawa_add_product(models.Model):
    user = models.CharField(max_length=50,null=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price  = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    descriptions = models.TextField(max_length=500)
    image = models.ImageField(upload_to="productImage",null=True)
    def __str__(self):
        return self.product_name


class medicin(models.Model):
    shop_name = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=20,null=True)
    category = models.CharField(max_length=20,null=True)
    price = models.CharField(max_length=20,null=True)
    Patient_name = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    quantity = models.CharField(max_length=21,null=True)
    added_on = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.Patient_name

class lab_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name
class lab_report(models.Model):
    user = models.CharField(max_length=100,null=True)
    fname = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    pin = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    purpose = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.fname

class lab_reply(models.Model):
    user =  models.CharField(max_length=50,null=True)
    phone =  models.CharField(max_length=50,null=True)
    status =  models.CharField(max_length=50,null=True)
    massage =  models.CharField(max_length=50,null=True)
    file =  models.FileField(upload_to="reportfile",null=True)

    def __str__(self):
        return self.user