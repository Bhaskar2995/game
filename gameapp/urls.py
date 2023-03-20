from .views import home
from django.urls import path


urlpatterns = [
    path('',home.as_view()),
    path('/<int:id>',home.as_view())
]