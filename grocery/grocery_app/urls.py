from django.urls import path
from .views import create_grocery_view,list_grocery_view,grocery_detail_view 
urlpatterns=[
    path('create-grocery/',create_grocery_view),
    path('list-grocery/',list_grocery_view),
    path('grocery-details/<int:id>/',grocery_detail_view)
]