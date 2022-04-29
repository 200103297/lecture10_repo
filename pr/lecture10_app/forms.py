from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Тақырып", widget=forms.TextInput(attrs={'class': 'form-input'}))
    author = forms.CharField(max_length=255, label="Автор", widget=forms.TextInput(attrs={'class': 'form-input'}))
    is_published = forms.BooleanField(label="Шығарылым", required=False, initial=True)
    place = forms.CharField(max_length=255, label="Шығарылған жері", widget=forms.TextInput(attrs={'class': 'form-input'}))
    date = forms.DateField(input_formats=['%d/%m/%Y'])
    slug = forms.SlugField(max_length=255, label="URL")
    desc = forms.CharField(max_length=1000, label="туралы", widget=forms.TextInput(attrs={'class': 'form-input'}))




