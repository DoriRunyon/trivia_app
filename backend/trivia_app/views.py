from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
import json

from .models import Game

# Create your views here.

def index(request, pk):
    template_name = 'trivia_app/index.html'

    return render(request, template_name)

def get_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game_name = game.name
    is_game_active = game.active 

    game = {
        "name": game.name,
        "active": is_game_active 
    }

    return HttpResponse(json.dumps(game))
