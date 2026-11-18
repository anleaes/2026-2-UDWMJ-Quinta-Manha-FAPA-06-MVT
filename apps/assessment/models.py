from django.db import models
from apps.core.models import Member, Employee

class Assessment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Membro")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="Profissional Responsável")
