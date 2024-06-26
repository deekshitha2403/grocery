from django.shortcuts import render
from grocery_app .models import Grocery , Order

from django.http import Http404

def dashboard_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render (request, "dashboard/home.html")
    else:
        raise Http404

def admin_grocery_list_view(request):
    queryset = Grocery.objects.all()
    context = {
        'grocerys':queryset
    }
    return render(request, 'dashboard/admin_grocery_list.html', context)

def admin_order_list_view(request):
    status = request.GET.get('status')
    queryset = Order.objects.all()
    if status == 'confirmed':
        print("confirmed")
        queryset = queryset.filter(status='order confirmed')
    context = {
        'orders':queryset
    }
    return render(request, 'dashboard/admin_order_list.html', context)


def admin_grocery_details(request, id):
    grocery = grocery.objects.get(id=id)
    context = {
        'grocerys' : grocery
    }
    return render(request, "dashbord/admin_grocery_details.html", context)
