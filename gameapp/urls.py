from .views import GameView
from django.urls import path


urlpatterns = [
    path('',GameView.as_view()),
    path('/<int:id>',GameView.as_view())
]