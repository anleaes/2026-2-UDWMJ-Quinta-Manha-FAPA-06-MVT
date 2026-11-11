from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    birth_date = models.DateField()
