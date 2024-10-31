from django.urls import path
from .views import VegetableListView, VegetableDetailView, SearchViewList, AddVegetable, VegetableUpdateView, VegetableDeleteView

urlpatterns = [
    path('', VegetableListView.as_view(), name = 'vegetable_list'),
    path('<uuid:pk>/', VegetableDetailView.as_view(), name='vegetable_detail'),
    path('search/', SearchViewList.as_view(), name='search' ),
    path('add/', AddVegetable.as_view(), name='add_vegetable'),
    path('edit/(?P<pk>[0-9]+)/\\Z', VegetableUpdateView.as_view(), name='edit_vegetable'),
    path('delete/(?P<pk>[0-9]+)/\\Z', VegetableDeleteView.as_view(), name='delete_vegetable'),
]