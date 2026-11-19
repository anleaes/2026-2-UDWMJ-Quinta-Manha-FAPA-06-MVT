from django.db import models
from django.core.validators import MinValueValidator


class ClassSession(models.Model):
    scheduled_at = models.DateTimeField(
        verbose_name="Data e horário"
    )

    duration_minutes = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Duração em minutos"
    )

    description = models.TextField(
        verbose_name="Descrição"
    )

    modality = models.ForeignKey(
        "modalities.Modality",
        on_delete=models.PROTECT,
        related_name="class_sessions",
        verbose_name="Modalidade"
    )

    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.PROTECT,
        related_name="class_sessions",
        verbose_name="Sala"
    )

    instructor = models.ForeignKey(
        "employees.Employee",
        on_delete=models.PROTECT,
        related_name="class_sessions",
        verbose_name="Instrutor"
    )

    class Meta:
        verbose_name = "Sessão de Aula"
        verbose_name_plural = "Sessões de Aula"
        ordering = ["scheduled_at"]

    def __str__(self):
        return f"{self.description} - {self.scheduled_at:%d/%m/%Y %H:%M}"
