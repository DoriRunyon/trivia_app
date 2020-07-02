from django.contrib import admin  # noqa

from .models import *

# Register your models here.

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Participant)
admin.site.register(ParticipantAnswer)
