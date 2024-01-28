import logging
import random

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        logger.info(f' функция {view.__name__} вернула {res.content.decode("utf-8")}')
        return res
    return wrapper


@log
def index(request):
    return HttpResponse("случайные числа")

@log
def orel(request):
    num = rnd(0, 1)
    if num == 0:
        # logger.info('решка')
        return HttpResponse("решка")
    # logger.info('орел')
    return HttpResponse("орел")

@log
def dice(request):
    num = rnd(1, 6)
    # logger.info(f'выпало {num}')
    return HttpResponse(f'выпало {num}')

@log
def rnd_(request):
    num = rnd(0, 100)
    # logger.info(f'выпало {num}')
    return HttpResponse(f'выпало {num}')


def rnd(start, stop):
    return random.randint(start, stop)
