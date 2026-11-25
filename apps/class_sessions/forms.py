from django import forms
from .models import ClassSession


class ClassSessionForm(forms.ModelForm):
    class Meta:
        model = ClassSession

        fields = [
            'scheduled_at',
            'duration_minutes',
            'description',
            'modality',
            'room',
            'instructor',
        ]

        widgets = {
            'scheduled_at': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}
            ),
            'duration_minutes': forms.NumberInput(
                attrs={'min': 1}
            ),
            'description': forms.Textarea(
                attrs={'rows': 4}
            ),
        }
