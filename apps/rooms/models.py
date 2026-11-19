from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    name = models.CharField('nome', max_length=100)
    capacity = models.IntegerField('capacidade', validators=[MinValueValidator(1)])
    is_available = models.BooleanField('disponível', default=True)
    photo = models.ImageField('foto', upload_to='rooms/', blank=True)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['name']

    def __str__(self):
        return self.name