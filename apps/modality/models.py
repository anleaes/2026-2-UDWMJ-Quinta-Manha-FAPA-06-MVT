from django.db import models


class Modality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    max_students = models.IntegerField()
    icon = models.ImageField(upload_to="modalities/icons/", blank=True, null=True)

    def __str__(self):
        return self.name