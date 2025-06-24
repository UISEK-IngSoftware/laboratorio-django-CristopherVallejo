from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.order_by('name')
    serializer_class = PokemonSerializer