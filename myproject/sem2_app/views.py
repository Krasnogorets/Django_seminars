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
def orel(request, num):
    num_lst = ["решка" if rnd(0, 1) == 0 else "орел" for _ in range(num)]
    context = {'num_lst': num_lst, 'title': 'орел-решка'}
    return render(request, "sem2_app/index.html", context)


@log
def dice(request, num):
    num_lst = [rnd(1, 6) for _ in range(num)]
    context = {'num_lst': num_lst, 'title': 'кубики'}
    return render(request, "sem2_app/index.html", context)


@log
def rnd_(request, num):
    num_lst = [rnd(0, 100) for _ in range(num)]
    context = {'num_lst': num_lst, 'title': 'случайные числа'}
    return render(request, "sem2_app/index.html", context)


def rnd(start, stop):
    return random.randint(start, stop)
