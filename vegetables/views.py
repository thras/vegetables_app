from .models import Vegetable
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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

class SearchViewList(LoginRequiredMixin, ListView):
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

class AddVegetable(LoginRequiredMixin, CreateView):
  model = Vegetable
  fields = '__all__'
  context_object_name = 'add_vegetable'
  def get_success_url(self):
    return reverse('vegetable_list')
  
class VegetableUpdateView(UpdateView):
  ''' View for update a Vehicle. '''
  model = Vegetable
  fields = '__all__'
  context_object_name = 'edit_vegetable'
  def get_success_url(self):
    return reverse('vegetable_list')

class VegetableDeleteView(DeleteView): 
  ''' View for delete a Vehicle.'''
  model = Vegetable
  success_url = reverse_lazy("vegetable_list")