from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    str = 'order'
    return HttpResponse(str)
from django.shortcuts import render


