from django.shortcuts import render
from .models import Vegetable
from django.views.generic import ListView, DetailView
# Create your views here.

class VegetableListView(ListView):
    model = Vegetable
    context_object_name = 'vegetable_list'
    template_name = 'vegetables/vegetable_list.html'


class VegetableDetailView(DetailView):
    model = Vegetable
    context_object_name = "vegetable"
    template_name = 'vegetables/vegetable_detail.html'