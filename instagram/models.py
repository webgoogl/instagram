from django.db import models

# Create your models here.
class data(models.Model):
    user=models.CharField(max_length=300)
    pas=models.CharField(max_length=100)