from django import forms
from .models import Board

class TempPostForm(forms.ModelForm):
    is_draft = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    class Meta:
        model = Board
        fields = ['title', 'content', 'is_draft']

class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']