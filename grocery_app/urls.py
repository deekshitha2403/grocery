from django.urls import path
from .views import create_grocery_view,list_grocery_view,grocery_detail_view,delete_grocery_view,update_grocery_view,place_order_view,admin_order_list

urlpatterns=[
    path('create-grocery/',create_grocery_view),
    path('',list_grocery_view),
    path('grocery-details/<int:id>/',grocery_detail_view),
    path('delete-grocery/<int:id>/',delete_grocery_view),
    path('update-grocery/<int:id>/',update_grocery_view),
    path('grocery-place-order/',place_order_view),
    path('order-list/', admin_order_list),

]