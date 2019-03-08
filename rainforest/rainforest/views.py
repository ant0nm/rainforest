from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product
from rainforest.forms import ProductForm


def root(request):
    return HttpResponseRedirect('products')


def list_products(request):
    return render(request, 'index.html', {
        'products': Product.objects.all()
    })


def show_product(request, id):
    return render(request, 'product.html', {
        'product': Product.objects.get(pk=id)
    })


def new_product(request):
    return render(request, 'new.html', {'form': ProductForm()})


def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'new.html', {
            'form': form
        })


def edit_view(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'edit.html', {'form': ProductForm(instance=product), 'product': product})


def edit_product(request, id):
    form = ProductForm(request.POST, instance=Product.objects.get(pk=id))
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'new.html', {
            'form': form
        })
    # return render(request, 'product.html', {'form': ProductForm(request.POST, instance=Product.objects.get(pk=id))})
