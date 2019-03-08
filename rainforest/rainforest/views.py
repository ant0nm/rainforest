from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product
from rainforest.forms import ProductForm
from django.core.exceptions import ValidationError


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
        new_product = form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'new.html', {
            'form': form
        })

        # html_string = render(request, 'new.html' {'errors': form.errors})
        # return HttpResponseRedirect(html_string)

        # return render(request, 'new.html', {'errors': form.errors})
        # context = {'errors': form.errors}
        # html_string = render(request, 'new.html', context)
        # return HttpResponseRedirect(html_string)
