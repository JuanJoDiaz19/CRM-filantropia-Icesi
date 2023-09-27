from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class New(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

class Allie_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Allie(models.Model):
    id = models.AutoField(primary_key=True)
    allie_type_id = models.ForeignKey(Allie_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    image_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class User(AbstractBaseUser):
    naame= models.CharField(max_length=50)
         
    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    allie = models.ForeignKey(Allie, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    aux_email = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
