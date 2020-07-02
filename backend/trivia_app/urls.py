from django.conf.urls import include, url  # noqa
from django.urls import path
from django.contrib import admin
from django.shortcuts import redirect
from . import views

import django_js_reverse.views


urlpatterns = [
    path("", lambda request : redirect("/trivia_app/")),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("trivia_app/", views.index),
]
