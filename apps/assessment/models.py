from django.db import models
from member.models import Member
from employee.models import Employee

class Assessment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Membro")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="Profissional Responsável")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    height = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Altura (m)")
    body_fat_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, verbose_name="% de Gordura")
    assessment_date = models.DateField(auto_now_add=True, verbose_name="Data da Avaliação")
    observations = models.TextField(blank=True, null=True, verbose_name="Observações")

    def __str__(self):
        return f"Avaliação de {self.member} em {self.assessment_date}"

    class Meta:
        verbose_name = "Avaliação Física"
        verbose_name_plural = "Avaliações Físicas"
