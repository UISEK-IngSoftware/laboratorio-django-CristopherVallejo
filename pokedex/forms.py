from django import forms
from .models import Pokemon
class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type1', 'weight', 'height', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Charmander'}),
            'type1': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Fuego'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': '8.5'}),
            'height': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': '60'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'id': 'image_field'
             }),
        }