from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")

# Create your views here.
def emploi(request):
    return HttpResponse('emploi')