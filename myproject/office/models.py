from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    salary=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    description=models.TextField(null=True)