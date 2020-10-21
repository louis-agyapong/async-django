import time, asyncio
from django.http import HttpResponse
from asgiref.sync import sync_to_async

from movies.models import Movie
from stories.models import Story

# helper functions
def get_movies():
    """
    Get movies
    """
    print("preparing to get the movies...")
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("Got all the movies")


def get_stories():
    """
    Get stories
    """
    print("preparing to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("Got all the stories")


@sync_to_async
def get_movies_async():
    """
    Get movies
    """
    print("preparing to get the movies...")
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("Got all the movies")


@sync_to_async
def get_stories_async():
    """
    Get stories
    """
    print("preparing to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("Got all the stories")


def home_view(request):
    """
    Home view
    """
    return HttpResponse("Hello world")


def main_view(request):
    """
    Main view
    """
    start_time = time.time()
    get_movies()
    get_stories()
    total = time.time() - start_time
    print("total: ", total)
    return HttpResponse("sync")


async def main_view_async(request):
    """
    Main view async
    """
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time() - start_time)
    print('total: ', total)
    return HttpResponse('async')