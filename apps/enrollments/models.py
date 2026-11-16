from django.db import models
from members.models import Member
from plans.models import Plan
from employees.models import Employee
# Create your models here.

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativa'),
        ('pending', 'Pendente'),
        ('canceled', 'Cancelada'),
        ('expired', 'Expirada'),
    ]