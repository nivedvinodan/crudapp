from django.db import models

# Create your models here.
class Task(models.Model):
    objects=None
    slno=models.IntegerField()
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)