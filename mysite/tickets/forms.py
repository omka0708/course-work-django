from django import forms
from .models import Ticket
from django.core.exceptions import ValidationError


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'type', 'email', 'event_idevent']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}, choices=[('Танцпол', 'Танцпол'), ('VIP', 'VIP')]),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
