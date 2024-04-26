from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "Register"


class feedback1(models.Model):
    firstname=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email=models.EmailField(primary_key=True)
    comment=models.TextField(max_length=255)
    class Meta:
        db_table="feedback1"
