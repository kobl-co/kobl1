from django.urls import re_path

from . import views

urlpatterns = [
    re_path('card/', views.card_list, name='card_list'),
	re_path('^$', views.index, name='index'),
]