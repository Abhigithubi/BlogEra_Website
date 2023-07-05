from django.db import models
from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    contact = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "Viewer"

class blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date_of_blog=models.DateTimeField(default=timezone.now)
    blogger=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'