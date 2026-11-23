from django.db import models
from person.models import Person


class Member(Person):
    gender = models.CharField('Gênero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    cpf = models.CharField('CPF', max_length=14)
    registered_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    photo = models.ImageField('Foto', upload_to='members/photos/', blank=True)
    medical_certificate = models.FileField(
        'Atestado médico',
        upload_to='members/certificates/',
        blank=True,
    )

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['id']

    def __str__(self):
        return super().__str__()