from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic



# Create your views here.

def index(request):
    return HttpResponse("Welcome to Dori's Trivia App!")

# class IndexView(generic.ListView):
#     template_name = 'trivia_app/index.html'

#     def get_queryset(self):
#         """
#         """
#         return None
