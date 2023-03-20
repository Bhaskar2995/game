from django.shortcuts import render
from django.views import View
from .models import Game
from django.http import JsonResponse
from django.core.serializers import serialize
import json


class home(View):
    def get(self,request,*args, **kwargs):
        print(kwargs)
        if 'id' in kwargs:
            game_id = kwargs['id']
            print(game_id)
            games = Game.objects.filter(id=game_id)
        else:
            games = Game.objects.all()
        serialized_data = serialize("json", games)
        serialized_data = json.loads(serialized_data)
        return JsonResponse(serialized_data, safe=False, status=200)
    def post(self,request,*args, **kwargs):
        games = Game.objects.all()
        return JsonResponse()
