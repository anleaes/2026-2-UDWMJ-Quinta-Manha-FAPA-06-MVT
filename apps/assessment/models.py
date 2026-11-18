from django.db import models
from apps.core.models import Member, Employee

class Assessment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Membro")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="Profissional Responsável")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    height = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Altura (m)")
    body_fat_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, verbose_name="% de Gordura")
