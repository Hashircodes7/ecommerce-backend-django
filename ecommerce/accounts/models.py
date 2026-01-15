from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    avatar=models.ImageField(upload_to='avatars/',null=True,blank=True)
    bio=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return  f"{self.user.username}'s profile"

