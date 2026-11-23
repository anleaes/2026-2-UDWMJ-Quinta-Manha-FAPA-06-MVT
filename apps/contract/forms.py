from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        exclude = ()
        widgets = {
            'signed_at': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
