# pokedex/forms.py
from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    # Cambiamos de ModelChoiceField a CharField
    # El campo 'trainer' del modelo lo dejamos como Foreign Key,
    # pero aquí en el formulario lo representamos como un CharField.
    trainer_name = forms.CharField(
        max_length=100,
        required=False, # Puede ser opcional, como tu Foreign Key
        label="Nombre del Entrenador", # Etiqueta para el campo de texto
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ash Ketchum'})
    )
     # Sobreescribimos el método save para manejar la lógica del entrenador
    def save(self, commit=True):
        pokemon = super().save(commit=False) # No guardamos el Pokemon todavía
        trainer_name = self.cleaned_data.get('trainer_name')

        if trainer_name:
            # Busca un entrenador existente o crea uno nuevo
            trainer, created = Trainer.objects.get_or_create(name=trainer_name)
            pokemon.trainer = trainer # Asigna el entrenador al Pokemon
        else:
            pokemon.trainer = None # Si no se proporciona nombre, el entrenador es nulo

        if commit:
            pokemon.save()
        return pokemon
    

    class Meta:
        model = Pokemon
        # Eliminamos 'trainer' de fields, porque lo vamos a manejar manualmente con 'trainer_name'
        fields = ['name', 'type1', 'weight', 'height', 'picture'] # Ya NO incluye 'trainer' aquí
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

   