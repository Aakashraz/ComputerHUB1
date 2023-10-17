from django import forms
from .models import Computer,ComputerBrand, ComputerGeneration


class ComputerBrandForm(forms.ModelForm):
    class Meta:
        model= ComputerBrand
        fields="__all__"
        

class ComputerGenerationForm(forms.ModelForm):
    class Meta:
        model= ComputerGeneration
        fields= "__all__"