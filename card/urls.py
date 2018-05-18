from django.urls import path

from . import views

app_name = 'card'
urlpatterns = [
    path('', views.card_list, name='card_list'),
	path('card/<int:id>/', views.card_detail, name='card_detail'),
	path('<int:id>/', views.card_detail, name='card_detail'),
	path('new/', views.card_new, name='card_new'),
]