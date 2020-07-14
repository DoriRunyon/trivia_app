from django.conf.urls import include, url  # noqa
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from . import views

import django_js_reverse.views


urlpatterns = [
    path("", lambda request : redirect("/trivia_app/")),
    path("int:pk/", views.index),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("<int:pk>/trivia_app/", views.index),
    path('<int:game_id>/get_game/', views.get_game, name='get_game'),
]
