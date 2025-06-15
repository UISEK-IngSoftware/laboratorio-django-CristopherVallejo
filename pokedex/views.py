from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Pokemon
from .forms import PokemonForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required   
# pokedex/views.py
 
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

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})
@login_required
def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokedex:index')
    return render(request, 'delete_pokemon.html', {'pokemon': pokemon})

class CustomLoginView(LoginView):
    template_name = 'login_form.html'