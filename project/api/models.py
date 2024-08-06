from django.db import models


class Snippet(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField()
    city=models.CharField(max_length=50)
    rollno=models.IntegerField()
    depratment=models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
# Create your models here.
