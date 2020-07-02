from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Game(models.Model):
    name = models.CharField(max_length=20)
    start_countdown_seconds = models.IntegerField()
    question_countdown_seconds = models.IntegerField()
    active = models.BooleanField()

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

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
