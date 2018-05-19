from django.urls import path

from . import views

app_name = 'image'
urlpatterns = [
	path('image/', views.image_manip, name='image_manip'),
]