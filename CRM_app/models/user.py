from django.db import models

class New(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title