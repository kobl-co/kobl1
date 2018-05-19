from django.shortcuts import render
#from .models import Blog

def blog_index(request):
    return render(request, 'blog/index.html', {})