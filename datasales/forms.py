from django import forms
from django.forms import ModelForm
from .models import Sales


class AddSalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['name', 'sales', 'date']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date'})


        }
