from django.shortcuts import render, redirect, get_object_or_404

from ideas.models import Idea
from ideas.forms import IdeaForm


def index(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/index.html', {'ideas': ideas})


def details(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/details.html', {'idea': idea})


def new(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('ideas-details', pk=instance.pk)
    else:
        form = IdeaForm()

    return render(request, 'ideas/new.html', {'form': form})
