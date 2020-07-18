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

# this needs to be for admin only
def update_game(request, game_id):
    pass

def submit_answer(request, answer_id, participant_id):
    pass

def create_participant(request, participant_name):
    pass

def get_participant_scores(request, game_id):
    pass

def get_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    try:
        game_name = game.name
        status = game.status

        game = {
            "name": game.name,
            "status": status,
            "question": '',
            "answers": '',
        }
        
        # this should return questions, answers { answer_id: { text: '', correct: bool }}, game countdown and question countdown seconds

        return HttpResponse(json.dumps(game))
    except (Game.DoesNotExist):
        error = { "message": "Game does not exist"}
        return HttpResponse(json.dumps(error))
