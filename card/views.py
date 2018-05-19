from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from .models import Card

def card_list(request):
	cards = Card.objects.order_by('-published_date')
	#[:5]
	return render(request, 'card/card_list.html', {'cards': cards})
	
def card_list_approved(request):
	cards = Card.objects.filter(status__exact='Approved').order_by('-published_date')
	return render(request, 'card/card_list.html', {'cards': cards})
	
def card_list_new(request):
	cards = Card.objects.filter(status__exact='New').order_by('-published_date')
	return render(request, 'card/card_list.html', {'cards': cards})

def card_list_checked(request):
	cards = Card.objects.filter(status__exact='Checked').order_by('-published_date')
	return render(request, 'card/card_list.html', {'cards': cards})
	
def card_list_rejected(request):
	cards = Card.objects.filter(status__exact='Rejected').order_by('-published_date')
	return render(request, 'card/card_list.html', {'cards': cards})
	
def card_detail(request, id):
    try:
        c = Card.objects.get(pk=id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    return render(request, 'card/card_detail.html', {'c': c})
	
def card_create(request):
    return render(request, 'card/card_create.html', {})