from django.shortcuts import render
from .utils import get_comic_info


def index(request):
    comic = get_comic_info(183559, '신의 탑')
    context = {
        'comic': comic,
    }
    return render(request, 'mychart/index.html', context)
