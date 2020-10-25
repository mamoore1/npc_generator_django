from .forms import CharForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = CharForm(request.POST)
        if form.is_valid():
            char_class = form.cleaned_data['char_class']
            level = form.cleaned_data['level']
            num_chars = form.cleaned_data['num_chars']
            return HttpResponseRedirect('/results/')

    else:
        form = CharForm()

    return render(request, 'npc_generator/index.html', {'form': form})