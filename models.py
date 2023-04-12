from django.db import models

# Create your models here.
class post(models.Model):
    name=models.CharField(max_length=50)
    phoneno=models.IntegerField()
    time=models.TimeField()
    date=models.DateField()
    location=models.IntegerField()
    gender=models.IntegerField()
    message=models.CharField(max_length=100)
    