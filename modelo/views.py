from logging import NullHandler
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

class ModeloIndex(ListView):
    model = NullHandler
    template_name = 'index.html'

def index(request):
    return render(request, 'modelo/index.html')

