from django.shortcuts import render

from django.http import HttpResponse
from src.main.models import User
from time import sleep, perf_counter
from math import sqrt


def index(request, extra_msg=None):
    return HttpResponse(f"Hello, world. You're at the Pichacky index. {extra_msg}")


def err_test(request, extra_msg=None):
    return HttpResponse("Testing errors", status=500)


def get_users(request, extra_msg=None):
    return HttpResponse('<br>'.join([str(x) for x in User.objects.all().values_list(named=True)]))


def compute(request, exponent, extra_msg=None):
    start = perf_counter()

    c = 0
    for i in range(10 ** exponent):
        c += sqrt(i)

    end = perf_counter()

    return HttpResponse(f'Computation took {end - start} seconds')
