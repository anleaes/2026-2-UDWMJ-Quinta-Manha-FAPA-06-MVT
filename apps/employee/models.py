
from django.db import models
from person.models import Person

# Create your models here.
class Employee(Person):
    position = models.CharField('Cargo', max_length=20, choices=[
        ('instrutor', 'Instrutor'),
        ('recepcionista', 'Recepcionista'),
        ('gerente', 'Gerente'),
    ])
    salary = models.DecimalField('Salário', max_digits=10, decimal_places=2)
    cref = models.CharField('CREF', max_length=30, blank=True)