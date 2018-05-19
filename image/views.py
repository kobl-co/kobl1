from django.shortcuts import render
#from .models import Wo

def image_manip(request):
    return render(request, 'image/image_manip.html', {})