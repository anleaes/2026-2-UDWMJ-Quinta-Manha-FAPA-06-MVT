from django.db import models
from django.utils import timezone
from apps.core.models import Member, ClassSession


class ClassBooking(models.Model):
    class StatusChoices(models.TextChoices):
        CONFIRMED = 'CONFIRMED', 'Confirmado'
        CANCELLED = 'CANCELLED', 'Cancelado'
        PENDING = 'PENDING', 'Pendente'

    
