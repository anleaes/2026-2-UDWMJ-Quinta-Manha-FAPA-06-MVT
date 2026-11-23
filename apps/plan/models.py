from django.db import models
from modality.models import Modality


class Plan(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    monthly_price = models.DecimalField('Preço mensal', max_digits=8, decimal_places=2)
    duration_months = models.IntegerField('Duração (meses)')
    is_active = models.BooleanField('Ativo', default=True)
    modalities = models.ManyToManyField(Modality, verbose_name='Modalidades')

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        ordering = ['id']

    def __str__(self):
        return self.name
