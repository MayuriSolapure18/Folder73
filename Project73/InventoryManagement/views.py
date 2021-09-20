from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm


def AddProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ShowProduct')

    template_name = 'addProduct.html'
    context={'form':form}
    return render(request,template_name,context)

def ShowProduct(request):
    prod = Product.objects.all()
    template_name = 'showProduct.html'
    context = {'prod':prod}
    return render (request,template_name,context)


def UpdateProduct(request,update):
    prod=Product.objects.get(id=update)
    form=ProductForm(instance=prod)
    if request.method =='POST':
        form=ProductForm(request.POST,inctance=prod)
        if form.is_valid():
            form.save()
            return redirect('showProduct')
    template_name='addProduct.html'
    context={'form':form}
    return render(request,template_name,context)


def DeleteProduct(request,delete):
    prod=Product.objects.get(id=delete)
    prod.delete()
    return redirect('showProduct')

