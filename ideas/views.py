from django.shortcuts import render, redirect, get_object_or_404

from ideas.models import Idea, Image
from ideas.forms import IdeaForm, CommentForm


def index(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/index.html', {'ideas': ideas})


def details(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.idea = idea
            instance.save()
            return redirect('ideas-details', pk=idea.pk)
    else:
        form = CommentForm()

    return render(request, 'ideas/details.html',
        {'idea': idea, 'form': form})


def new(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for image in images:
                file_instance = Image(file=image, idea=instance)
                file_instance.save()
            return redirect('ideas-details', pk=instance.pk)
    else:
        form = IdeaForm()

    return render(request, 'ideas/new.html', {'form': form})
