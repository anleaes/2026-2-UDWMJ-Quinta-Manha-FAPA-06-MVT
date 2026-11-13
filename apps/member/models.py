from django.db import models
from person.models import Person

# Create your models here.
class Member(Person):
    gender = models.CharField('Gênero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
     
cpf = models.CharField('CPF', max_length=14)
registered_at = models.DateTimeField('Data de cadastro', auto_now_add=True)