from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        empty_label="Select option"
    )

    class Meta:
        model = Employee
        fields = ['full_name', 'mobile_no', 'position']
        labels = {'full_name': 'FULL NAME', 'mobile_no': 'MOBILE NUMBER', 'position': 'POSITION'}

