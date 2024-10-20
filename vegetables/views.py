from .models import Vegetable
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

class VegetableListView(LoginRequiredMixin, ListView):
    model = Vegetable
    paginate_by = 8
    context_object_name = 'vegetable_list'
    template_name = 'vegetables/vegetable_list.html'
    login_url = "login"


class VegetableDetailView(LoginRequiredMixin, DetailView):
    model = Vegetable
    context_object_name = "vegetable"
    template_name = 'vegetables/vegetable_detail.html'
    login_url = "login"

class SearchViewList(ListView):
    model = Vegetable
    paginate_by = 8
    context_object_name = 'vegetable_list'
    template_name = 'vegetables/search.html'

    def querystring(self):
        query = self.request.GET.copy()
        query.pop(self.page_kwarg, None)
        return query.urlencode()

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Vegetable.objects.filter(
            Q(name__icontains = query)|Q(category__icontains = query)
        )

class AddVegetable(CreateView):
  ''' View to add a new Vehicle.'''
  model = Vegetable
  fields = '__all__'
  context_object_name = 'add_vegetable'
  def get_success_url(self):
    return reverse('vegetable_list')