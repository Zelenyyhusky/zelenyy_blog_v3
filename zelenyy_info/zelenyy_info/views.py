from django.http import HttpResponse
from django.shortcuts import render

from random import randint


def index(request):

    number = randint(0, 100)

    return render(request, "zelenyy_info/index.html", {"randnum": number})