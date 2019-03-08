from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product

def show_products(request):
    products = Product.objects.all()
    context = {'products': products}
    html_string  = render(request, 'index.html', context)
    return HttpResponse(html_string)
