from django.db import models
from django.utils import timezone
# Ajusta os imports dos modelos Member e ClassSession conforme o app onde eles estão criados (ex: core)
from member.models import Member

class ClassBooking(models.Model):
    class StatusChoices(models.TextChoices):
        CONFIRMED = 'CONFIRMED', 'Confirmado'
        CANCELLED = 'CANCELLED', 'Cancelado'
        PENDING = 'PENDING', 'Pendente'

    booked_at = models.DateTimeField('Data do Agendamento', default=timezone.now)
    attended = models.BooleanField('Compareceu', default=False)
    status = models.CharField(
        'Status',
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.CONFIRMED
    )
    member = models.ForeignKey(Member, verbose_name='Membro', on_delete=models.CASCADE)
    #class_session = models.ForeignKey(ClassSession, verbose_name='Sessão de Aula', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['id']

    def __str__(self):
        return f"Agendamento de {self.member} para {self.class_session}"