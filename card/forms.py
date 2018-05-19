from django import forms
from django.utils import timezone

class CardForm(forms.Form):
 #   author = forms.CharField(label='author', max_length=100)
 #   id = forms.AutoField(primary_key=True)
    contact_person = forms.CharField(label='contact', max_length=200)
    title = forms.CharField(label='title', max_length=200)
    text = forms.CharField(label='text')
    functional_location = forms.CharField(label='f.loc', max_length=200)
#    created_date = forms.DateField(label='Your name')
#    published_date = forms.DateField(label='Your name')
 #   status = forms.CharField(label='status', max_length = 200)