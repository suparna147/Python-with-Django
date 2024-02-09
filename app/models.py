from django.db import models

# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=20)
    mobno=models.IntegerField(null=True)
    email=models.CharField(max_length=20)
    pwrd=models.CharField(max_length=20)

class Libms(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    mobno = models.IntegerField(null=True)
    email = models.CharField(max_length=20)
    bokname = models.CharField(max_length=20)
    autname = models.CharField(max_length=20)
    bordt = models.DateTimeField()
    retdt = models.DateTimeField()