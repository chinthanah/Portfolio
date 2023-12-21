from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Phone=models.CharField(max_length=30)
    Textarea=models.TextField()