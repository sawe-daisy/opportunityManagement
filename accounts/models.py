from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
    # def save(self):
    #     return self.save()
    
    # def delete(self):
    #     return self.delete()

    def get_absolute_url(self):
        return reverse('home')

class Account(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=40)



     