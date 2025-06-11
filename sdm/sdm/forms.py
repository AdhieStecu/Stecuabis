from django import forms
from .models import Book

class TaskForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title','Author','published date']
