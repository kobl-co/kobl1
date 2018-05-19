from django.shortcuts import render
#from .models import Wo

def wo_status_update(request):
    return render(request, 'wo/wo_status.html', {})