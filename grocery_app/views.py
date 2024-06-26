from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Grocery,Order

def create_grocery_view(request):
    if request.method=='POST':
        grocery_n=request.POST['grocery_name']
        prize=request.POST['prize']
        grocery_image=request.FILES['image']
        grocery=Grocery(grocery_name=grocery_n,prize=prize,image=grocery_image)
        grocery.save()
        messages.success(request," grocery created successfully")
    return render(request,'grocery/create_grocery.html')

def list_grocery_view(request):
    grocery_lists=Grocery.objects.all()
    return render(request,'grocery/list_grocery.html',{'grocery_list':grocery_lists})

    
def grocery_detail_view(request,id):
    details=Grocery.objects.get(id=id)
    return render(request,'grocery/grocery_details.html',{'detail':details})

def delete_grocery_view(request,id):
    gro=Grocery.objects.get(pk=id)
    gro.delete()
    return redirect('/list-grocery/')

def update_grocery_view (request,id):
    gro=Grocery.objects.get(pk=id)
    if request.method == "POST":
        grocery_n=request.POST['grocery_name']
        prize=request.POST['prize']
        image=request.FILES['image']
        gro.grocery_name=grocery_n
        gro.prize=prize
        gro.image=image
        gro.save()
        messages.success(request," grocery updated successfully")
        return redirect("/")
        
    return render(request, "grocery/update_grocery.html",{'grocery':gro})

def place_order_view(request):
    if request.method == "POST":
        id = request.POST["grocery_id"]
        obj = Grocery.objects.get(pk=id)
        Order.objects.create(user=request.user, grocery=obj)
    return redirect("/")


    
def admin_order_list(request): 
    gro = Order.objects.all()
    return render(request, "admin/order_list.html", {'grocery' : gro})
