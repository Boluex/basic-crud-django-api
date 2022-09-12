from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='user_profile')
    number=models.CharField(max_length=2000,blank=True)
    nickname=models.CharField(max_length=2000,blank=True)
    age=models.CharField(max_length=2000,blank=True)