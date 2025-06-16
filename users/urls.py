from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("signin/", signin),
    path("signup/", signup),
]