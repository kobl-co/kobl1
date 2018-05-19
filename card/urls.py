from django.urls import path

from . import views

app_name = 'card'
urlpatterns = [

	path('card/<int:id>/', views.card_detail, name='card_detail'),
#	path('<int:id>/', views.card_detail, name='card_detail'),
	path('create/', views.card_create, name='card_create'),
	path('approved/', views.card_list_approved, name='card_list_approved'),
	path('checked/', views.card_list_checked, name='card_list_checked'),
	path('rejected/', views.card_list_rejected, name='card_list_rejected'),
	path('new/', views.card_list_new, name='card_list_new'),
	path('', views.card_list, name='card_list'),
#	path('submit/', views.card_submit, name='card_submit'),
]