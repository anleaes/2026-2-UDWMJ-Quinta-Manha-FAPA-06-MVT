from django.db import models
from enrollment.models import Enrollment

# Create your models here.

class Payment(models.Model):
    METHOD_CHOICES = [
        ('pix', 'Pix'),
        ('credit', 'Cartão de crédito'),
        ('debit', 'Cartão de débito'),
        ('boleto', 'Boleto'),
        ('cash', 'Dinheiro'),
    ]

    due_date = models.DateField('Vencimento', auto_now=False, auto_now_add=False)
    paid_at = models.DateTimeField('Pago em', null=True, blank=True)
    amount = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    method = models.CharField('Forma de pagamento', max_length=10, choices=METHOD_CHOICES, default='pix')
    receipt = models.FileField('Comprovante', upload_to='docs', null=True, blank=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']