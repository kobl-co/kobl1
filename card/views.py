#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the card index.")
	
def card_list(request):
    return render(request, 'card/card_list.html', {})