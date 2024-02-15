from django.shortcuts import render

from django.http import HttpResponse
from src.main.models import User


def index(request, extra_msg=None):
    return HttpResponse(f"Hello, world. You're at the Pichacky index. {extra_msg}")


def err_test(request, extra_msg=None):
    return HttpResponse("Testing errors", status=500)


def get_users(request, extra_msg=None):
    return HttpResponse('<br>'.join([str(x) for x in User.objects.all().values_list(named=True)]))
