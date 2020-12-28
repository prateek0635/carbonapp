from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_prof(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='media/')
    bio=models.TextField(max_length=1000)


class post_image(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.ImageField( upload_to='media/')
    caption=models.CharField(max_length=200)