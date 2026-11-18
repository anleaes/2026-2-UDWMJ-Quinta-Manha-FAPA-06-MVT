from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ()
        widgets = {
            'birth_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'},
            ),
        }