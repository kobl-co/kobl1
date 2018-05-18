#from django.http import HttpResponse
from django.shortcuts import render
#from django.utils import timezone
#from django.template import loader
#from .models import Card


def index(request):
    return render(request, 'index/index.html', {})
