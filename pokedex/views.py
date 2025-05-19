from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
# Create your views here.   
def index(request):
    pokemons = Pokemon.objects.order_by('name')
    # pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))