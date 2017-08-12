from django.shortcuts import render
from django.shortcuts import render
from .models import *

def index(request):
    page = 'knopka'
    knopka_places = Knopka.objects.all()
    return render(request, 'index.html', {'page': page, 'knopka_places': knopka_places})

