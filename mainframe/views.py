from django.shortcuts import render
from django.http import HttpResponse


def mapa(request):
    return render(request, 'pages/index.html')