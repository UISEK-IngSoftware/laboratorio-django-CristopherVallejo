# pokedex/admin.py
from django.contrib import admin
from .models import Pokemon, Trainer # <--- ¡Asegúrate de importar Trainer aquí!

# Registra tus modelos aquí.
admin.site.register(Pokemon)
admin.site.register(Trainer) # <--- ¡Añade esta línea para registrar el modelo Trainer!