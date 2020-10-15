from django.shortcuts import render

from django.http import HttpResponse


def index(request, foo=None):
    return HttpResponse(f"Hello, world. You're at the Pichacky index. {request}, {foo}")
