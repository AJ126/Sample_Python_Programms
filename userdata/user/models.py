from django.db import models

# Create your models here.
class userinfo(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    pincode=models.IntegerField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phoneno=models.IntegerField(max_length=50)
