from django.urls import path
from .views import VegetableListView, VegetableDetailView

urlpatterns = [
    path('', VegetableListView.as_view(), name = 'vegetable_list'),
    path('<uuid:pk>/', VegetableDetailView.as_view(), name='vegetable_detail'),
]