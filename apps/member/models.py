from django.db import models
from person.models import Person

# Create your models here.
class Member(Person):
    gender = models.CharField('Gênero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])