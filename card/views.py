from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from .models import Card

def card_list(request, card_status):
	if card_status=='approved':
		cards = Card.objects.filter(status__exact=card_status).order_by('-published_date')
	else:
		cards = Card.objects.order_by('-published_date')
		#[:5]
	return render(request, 'card/card_list.html', {'cards': cards})

def card_detail(request, id):
    try:
        c = Card.objects.get(pk=id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    return render(request, 'card/card_detail.html', {'c': c})
	
def card_new(request):
    return render(request, 'card/card_new.html', {})