from django.db import models
from django.utils import timezone
from apps.core.models import Member, ClassSession


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
    class_session = models.ForeignKey(ClassSession, verbose_name='Sessão de Aula', on_delete=models.CASCADE)
