from django.shortcuts import render

from django.http import HttpResponse


def index(request, extra_msg=None):
    return HttpResponse(f"Hello, world. You're at the Pichacky index. {extra_msg}")
