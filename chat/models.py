from django.db import models

from django.contrib.auth.models import User
 
class Comments(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=255)
    
class Mess(models.Model):
    text = models.CharField(max_length=255)    