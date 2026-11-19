from django.contrib import admin
from .models import ClassSession


@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "scheduled_at",
        "duration_minutes",
        "modality",
        "room",
        "instructor",
    )

    list_filter = (
        "scheduled_at",
        "modality",
        "room",
        "instructor",
    )

    search_fields = (
        "description",
        "modality__name",
        "room__name",
    )

    ordering = ("scheduled_at",)
