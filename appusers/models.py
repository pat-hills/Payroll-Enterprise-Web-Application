from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models 

# Create your models here.

class User(AbstractUser):
    is_password_change = models.BooleanField(default=True)
    account_type = models.TextField(blank=False,max_length=64)
    user_role = models.TextField(blank=False,max_length=128)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)


   






    



