from django.db import models

# Create your models here.

class Users(models.Model):
    uname=models.CharField(max_length=20)
    uemail=models.CharField(max_length=40)
    upass=models.CharField(max_length=20)
    def __str__(self):
        return self.uname

