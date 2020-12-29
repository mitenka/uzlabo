from django import forms
from django.forms import ModelForm

from ideas.models import Idea


class IdeaForm(ModelForm):
    images = forms.FileField(required=False, widget=forms.ClearableFileInput(
        attrs={'multiple': True}))

    class Meta:
        model = Idea
        fields = [
            'category',
            'subcategory',
            'title',
            'description',
            'address',
            'images'
        ]
