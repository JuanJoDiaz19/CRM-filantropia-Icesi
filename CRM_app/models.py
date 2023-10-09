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
    
class Area(models.Model):
    id = models.AutoField(primary_key=True)
    area_description = models.CharField(max_length=50)

    def __str__(self):
        return self.area_description
    
class Allie(models.Model):
    id = models.AutoField(primary_key=True)
    allie_type_id = models.ForeignKey(Allie_Type, on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    image_link = models.CharField(max_length=200)
    description= models.CharField(max_length=500, null=True)

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
    
class Event_Type(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Event(models.Model):
    id= models.AutoField(primary_key=True)
    event_type_id= models.ForeignKey(Event_Type,on_delete=models.CASCADE)
    date= models.DateField()
    name= models.CharField(max_length=20)
    objective= models.CharField(max_length=200)
    description= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class EventAllie(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    allie = models.ForeignKey(Allie, on_delete=models.CASCADE)

    class Meta:
        db_table = 'EVENT_ALLIE'
        unique_together = (('event', 'allie'),)
    
    def __str__(self):
        return self.name
    
class Investigation_Project(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=20)
    description= models.CharField(max_length=200)
    active= models.TextField(max_length=1)
    start_date= models.DateField()
    finish_date= models.DateField()
    
    def __str__(self):
        return self.name
    

class Publication(models.Model):
    id=models.AutoField(primary_key=True)
    investigation_project_id= models.ForeignKey(Investigation_Project,on_delete=models.CASCADE)
    doi= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class AllieProject(models.Model):
    investigation_project= models.ForeignKey(Investigation_Project, on_delete=models.CASCADE)
    allie= models.ForeignKey(Allie,on_delete=models.CASCADE)

    class Meta:
        db_table = 'ALLIE_PROJECT'
        unique_together = (('allie', 'investigation_project'),)
    
    def __str__(self):
        return self.name


class Donation_Type(models.Model):
    id= models.AutoField(primary_key=True)
    max_value= models.IntegerField()
    min_value= models.IntegerField()
    name= models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Donation(models.Model):
    id= models.AutoField(primary_key=True)
    date= models.DateField()
    amount= models.IntegerField()
    donation_type_id= models.ForeignKey(Donation_Type,on_delete=models.CASCADE)
    allie_id= models.ForeignKey(Allie,on_delete=models.CASCADE)
    description= models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    
class Meeting_type(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=20)
    def __str__(self):
        return self.name
    

class Meeting(models.Model):
    id=models.AutoField(primary_key=True)
    allie_id= models.ForeignKey(Allie,on_delete=models.CASCADE)
    date= models.DateField()
    title= models.CharField(max_length=20)
    description=models.CharField(max_length=200, null= True)
    objective= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class Gender(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    
class Career(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    
class Practicing(models.Model):
    id= models.CharField(max_length=20, primary_key=True)
    allie_id= models.ForeignKey(Allie,on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    position= models.CharField(max_length=20)
    image_link = models.CharField(max_length=200, null=True)
    career_id= models.ForeignKey(Career,on_delete=models.CASCADE)
    gender_id= models.ForeignKey(Gender, on_delete=models.CASCADE)
    
    