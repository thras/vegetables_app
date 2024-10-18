from .models import Vegetable
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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