from django.shortcuts import render
from django.core.cache import cache
from .models import HelloWorldModel

def hello_world_view(request):
    hello_world_from_db = HelloWorldModel.objects.first().text # this will pick the first object from our database (in this case Hello World) and convert it in text and store it in hello_world_from_db

    cached_hello_world = cache.get('hello_world_key')  # hello_world_key id not found so it will return None

    if not cached_hello_world:
        cache.set('hello_world_key', hello_world_from_db) # this will set the text from hello_world_from_db in cache under the key hello_world_key

    context = {
        'hello_world_from_db': hello_world_from_db,
        'cached_hello_world': cached_hello_world,
    }
    return render(request, 'hello_world_template.html', context)

