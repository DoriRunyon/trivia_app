from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Game(models.Model):
    name = models.CharField(max_length=20)
    start_countdown_seconds = models.IntegerField()
    question_countdown_seconds = models.IntegerField()

    SHOW_WELCOME = 'SHOW_WELCOME'
    SHOW_QUESTION = 'SHOW_QUESTION'
    SHOW_LEADERBOARD = 'SHOW_LEADERBOARD'
    INACTIVE = 'INACTIVE'
    STATUS_CHOICES = [
        (SHOW_WELCOME, 'show welcome'),
        (SHOW_QUESTION, 'show question'),
        (SHOW_LEADERBOARD, 'show leaderboard'),
        (INACTIVE, 'inactive'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=INACTIVE,
    )

    def deactivate(self):
        # self.status = INACTIVE
        # and set all questions to used == False
        pass

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Participant(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class ParticipantAnswer(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    score = models.IntegerField()
