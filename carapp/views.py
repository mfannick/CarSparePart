from django.shortcuts import render,redirect
from .models import SpareParts,CarCategory,Cart

# Create your views here.

def homePage(request):
    categories=CarCategory.objects.all()
    spareParts=SpareParts.objects.all()
    context={
        'categories':categories,
        'spareParts':spareParts
    }
    return render(request,'spare/spare.html',context)


def carDetails(request,carId):
    category=CarCategory.objects.get(id=carId)
    spareParts=SpareParts.objects.filter(carCat=category)
    context={
        'carCats':spareParts
    }
    return render(request,'spare/spare.html',context)


def cart(request):
    sparePart=Cart.objects.all()[0]
    context={
        'sparePs':sparePart,
    }
    return render (request,'order.html',context)

def addToCart(request,spareId):
    spareParts=Cart.objects.all()[0]
    sparePart=SpareParts.objects.get(id=spareId)
    if not spareParts in spareParts.sparePart.all():
        spareParts.sparePart.add(sparePart)
    else:
        spareParts.sparePart.remove(sparePart)
    newTotal=0
    for spareP in spareParts.sparePart.all():
        newTotal+=spareP.price
        spareParts.total=newTotal
        spareParts.save()
    return redirect('cart')
def delete(request, cartId):
    cart = Cart.objects.get(sparePart__id=cartId)
    cart.delete()
    return redirect('homePage')