from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


def ice_cream_list(request):
    return HttpResponse('Список мороженого')


def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')
