#from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#    return HttpResponse("Hello, world. You're at the card index.")
	
def card_list(request):
    return render(request, 'card/card_list.html', {})