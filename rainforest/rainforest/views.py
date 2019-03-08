from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product
from rainforest.forms import ProductForm


def root(request):
    return HttpResponseRedirect('products')


def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    html_string = render(request, 'index.html', context)
    return HttpResponse(html_string)


def show_product(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    html_string = render(request, 'product.html', context)
    return HttpResponse(html_string)

def new_product(request):
    context = {
        'form': ProductForm()
    }
    html_string = render(request, 'new.html', context)
    return HttpResponse(html_string)

def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        new_product = form.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors)
