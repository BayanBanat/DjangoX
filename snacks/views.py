from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.
class SnacksListView(ListView):
    template_name='snacks/snakslist.html'
    model = Snack

class SnacksDetailView(DetailView):
    template_name='snacks/snaksdetail.html'
    model = Snack

class SnacksCreateView(CreateView):
    template_name='snacks/createsnaks.html'
    model = Snack
    fields = ['title','purcheser','description','url_image']

class SnacksDeleteView(DeleteView):
    template_name='snacks/deletesnaks.html'
    model = Snack
    success_url = reverse_lazy('snakslist')

class SnacksUpdateView(UpdateView):
    template_name='snacks/updatesnaks.html'
    model = Snack
    fields = ['title','description']
    success_url = reverse_lazy('snakslist')