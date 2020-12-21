from django.forms import ModelForm

from ideas.models import Idea


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = [
            'category',
            'subcategory',
            'title',
            'description',
            'address'
        ]
