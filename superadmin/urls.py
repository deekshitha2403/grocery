from django.urls import path
from .views import (dashboard_view, admin_grocery_list_view,admin_order_list_view )

app_name = "superadmin"
urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('grocery-list/', admin_grocery_list_view, name='admin_grocery_list'),
    path('order-list/', admin_order_list_view, name='admin_order_list'),
]

