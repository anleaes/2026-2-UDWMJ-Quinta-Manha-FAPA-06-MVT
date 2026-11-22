from django import forms
from .models import Modality


class ModalityForm(forms.ModelForm):

    class Meta:
        model = Modality
        exclude = ()