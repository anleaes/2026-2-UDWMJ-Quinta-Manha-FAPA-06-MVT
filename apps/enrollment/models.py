from django.db import models
from member.models import Member
#from plan.models import Plan
from employee.models import Employee

# Create your models here.

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativa'),
        ('pending', 'Pendente'),
        ('canceled', 'Cancelada'),
        ('expired', 'Expirada'),
    ]

    created_at = models.DateTimeField('Criada em', auto_now_add=True)
    start_date = models.DateField('Data de início', auto_now=False, auto_now_add=False)
    end_date = models.DateField('Data de término', auto_now=False, auto_now_add=False)
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    #plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['id']

    def __str__(self):
        return f'{self.member}'