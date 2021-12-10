from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    profile=CloudinaryField('profile')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    class Meta:
        ordering=['-profile']
