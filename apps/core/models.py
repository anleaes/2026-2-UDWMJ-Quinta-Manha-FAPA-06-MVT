from django.db import models


class Modality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    max_students = models.IntegerField()
    icon = models.ImageField(upload_to="modalities/icons/", blank=True, null=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_months = models.IntegerField()
    is_active = models.BooleanField(default=True)
    modalities = models.ManyToManyField(Modality, related_name="plans")

    def __str__(self):
        return self.name