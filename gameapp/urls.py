from .views import Game
from django.urls import path


urlpatterns = [
    path('',Game.as_view()),
    path('/<int:id>',Game.as_view())
]