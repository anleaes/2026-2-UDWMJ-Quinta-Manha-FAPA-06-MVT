from django.db import models


class Modality(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    max_students = models.IntegerField('Máximo de alunos')
    icon = models.ImageField('Ícone', upload_to='modality/icons/', blank=True, null=True)

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['id']

    def __str__(self):
        return self.name