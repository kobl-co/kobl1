from django.urls import path

from . import views

app_name = 'wo'
urlpatterns = [
	path('wo/status/', views.wo_status_update, name='wo_status_update'),
]