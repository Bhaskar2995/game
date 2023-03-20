from django.shortcuts import render
from django.views import View
from .models import Game
from django.http import JsonResponse
from django.core.serializers import serialize
import json
# from django.views.decorators.csrf import csrf_exempt

class home(View):
    def get(self,request,*args, **kwargs):
        data =[]
        if 'id' in kwargs:
            game_id = kwargs['id']
            games = Game.objects.filter(id=game_id)
            if not len(games) > 0:
                return JsonResponse({'error': "No entry found"})
        else:
            games = Game.objects.all()
            
        for game in games:
            dict = {'name': game.name, 'url':game.url, 'author':game.author, 'published_date':game.published_date}
            data.append(dict)

        return JsonResponse(data, safe=False, status=200)
    
    def post(self,request,*args, **kwargs):
        game = json.loads(request.body)
        games = Game(
            name = game['name'],
            url = game['url'],
            author = game['author'],
            published_date = game['published_date']
        )
        games.save()
        return JsonResponse({'success':"Data added successfully"}, safe=False, status=200)

    def put(self,request,*args, **kwargs):
        game_id = kwargs['id']
        data = json.loads(request.body)
        try:
            game = Game.objects.get(id=game_id)
        except:
            return JsonResponse({'error': "No entry found"})
        game.name = data['name']
        game.url = data['url']
        game.author = data['author']
        game.published_date = data['published_date']
        game.save()
        return JsonResponse({'success':'Data changed successfully'})
     
    def delete(self,request,*args,**kwargs):
        game_id = kwargs['id']
        data = json.loads(request.body)
        try:
            game = Game.objects.get(id=game_id)
            game.delete()
        except:
            return JsonResponse({'error': "No entry found"})
        return JsonResponse({'success':'Game with id %s successfully deleted' %game_id})

        