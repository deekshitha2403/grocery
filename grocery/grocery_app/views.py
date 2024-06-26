from django.shortcuts import render
from django.contrib import messages
from .models import Grocery

def create_grocery_view(request):
    if request.method=='POST':
        grocery_n=request.POST['grocery_name']
        prize=request.POST['prize']
        grocery_image=request.FILES['image']
        grocery=Grocery(grocery_name=grocery_n,prize=prize,image=grocery_image)
        grocery.save()
    return render(request,'create_grocery.html')

def list_grocery_view(request):
    grocery_lists=Grocery.objects.all()
    return render(request,'list_grocery.html',{'grocery_list':grocery_lists})

    
def grocery_detail_view(request,id):
    details=Grocery.objects.get(id=id)
    return render(request,'grocery_details.html',{'detail':details}) 
