from django.db import models

# Create your models here.
class candidate(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()
    first_round=models.IntegerField()
    second_round=models.IntegerField()
    third_round=models.IntegerField()
