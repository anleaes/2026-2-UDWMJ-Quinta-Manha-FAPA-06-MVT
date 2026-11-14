from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ()
        widgets = {
            'birth_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'},
            ),
        }