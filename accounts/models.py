from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    firstName= models.CharField(max_length=20, null=False)
    email=models.EmailField(null='false')
    username=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
    
    # def save(self):
    #     return self.save()
    
    # def delete(self):
    #     return self.delete()

    def get_absolute_url(self):
        return reverse('account')

class Account(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    address=models.CharField(max_length=40)
    image= CloudinaryField(default='image.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account')



     