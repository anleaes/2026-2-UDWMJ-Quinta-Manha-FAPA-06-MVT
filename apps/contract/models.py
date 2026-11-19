from django.db import models
from enrollment.models import Enrollment

# Create your models here.

class Contract(models.Model):
    number = models.CharField('Número', max_length=30, unique=True)
    signed_at = models.DateField('Data de assinatura', auto_now=False, auto_now_add=False, null=True, blank=True)
    is_signed = models.BooleanField('Assinado', default=False)
    pdf = models.FileField('PDF do contrato', upload_to='docs', null=True, blank=True)
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.number}'  