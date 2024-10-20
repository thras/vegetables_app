from django.urls import path
from .views import VegetableListView, VegetableDetailView, SearchViewList, AddVegetable

urlpatterns = [
    path('', VegetableListView.as_view(), name = 'vegetable_list'),
    path('<uuid:pk>/', VegetableDetailView.as_view(), name='vegetable_detail'),
    path('search/', SearchViewList.as_view(), name='search' ),
    path('add/', AddVegetable.as_view(), name='add_vegetable'),
]