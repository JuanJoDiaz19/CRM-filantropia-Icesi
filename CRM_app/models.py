from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, name, password=None, user_type=None, **extra_fields):
        if not name:
            raise ValueError('El campo de nombre es obligatorio')
        user = self.model(
            name=name,
            **extra_fields
        )
        user.set_password(password)
        #user.set_user_type(user_type)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(name, password, **extra_fields)
    
class User_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Agregado
    is_superuser = models.BooleanField(default=False)  # Agregado
    user_type_id= models.ForeignKey(User_Type, on_delete=models.CASCADE, default=1)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name

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
    objetivos= models.CharField(max_length=200,null=True)
    active= models.TextField(max_length=1)
    start_date= models.DateField()
    finish_date= models.DateField(null=True)
    
    def __str__(self):
        return self.name
    

class Publication(models.Model):
    id=models.AutoField(primary_key=True)
    investigation_project_id= models.ForeignKey(Investigation_Project,on_delete=models.CASCADE)
    doi= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    date= models.DateField(null=True)
    
    def __str__(self):
        return self.name
    

class AllieProject(models.Model):
    investigation_project= models.ForeignKey(Investigation_Project, on_delete=models.CASCADE)
    allie= models.ForeignKey(Allie,on_delete=models.CASCADE)

    class Meta:
        db_table = 'ALLIE_PROJECT'
        unique_together = (('allie', 'investigation_project'),)
    
    def __str__(self):
        return self.allie.name


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
    meeting_type_id= models.ForeignKey(Meeting_type, on_delete=models.CASCADE)
    date= models.DateField()
    title= models.CharField(max_length=20)
    description=models.CharField(max_length=200, null= True)
    objective= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Valida que solo uno de los dos campos (event o meeting) esté establecido
        if (self.event is None and self.meeting is None) or (self.event and self.meeting):
            raise ValidationError('Un comentario debe estar asociado a un evento o una reunión, pero no a ambos.')

    def save(self, *args, **kwargs):
        self.clean()
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.contenido   
    
class Gender(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    
class Career(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.id
    
class Practicing(models.Model):
    id= models.CharField(max_length=20, primary_key=True)
    allie_id= models.ForeignKey(Allie,on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    position= models.CharField(max_length=20)
    image_link = models.CharField(max_length=200, null=True)
    career_id= models.ForeignKey(Career,on_delete=models.CASCADE)
    gender_id= models.ForeignKey(Gender, on_delete=models.CASCADE)
    
    
    