from django import forms
from .models import donation

class donate(forms.ModelForm):
    class Meta:
        model=donation
        fields="__all__"