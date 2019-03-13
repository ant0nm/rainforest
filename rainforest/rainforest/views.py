from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import Product, Review
from rainforest.forms import ProductForm, ReviewForm
from django.urls import reverse


def root(request):
    return HttpResponseRedirect('products')


def list_products(request):
    return render(request, 'index.html', {
        'products': Product.objects.all()
    })


def show_product(request, product_id):
    return render(request, 'product.html', {
        'product': Product.objects.get(pk=product_id),
        'form': ReviewForm()
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


def edit_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'edit.html', {'form': ProductForm(instance=product), 'product': product})


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'edit.html', {
            'form': form,
            'product': product
        })

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return HttpResponseRedirect('/')


def create_review(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.instance
        review.product = product
        review.save()
        return HttpResponseRedirect(reverse('show_product', args=[product_id]))
    else:
        context = {'form': form}
        return render(request, 'product.html', context)

def edit_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    product = review.product
    form = ReviewForm(instance=review)
    context = {'form': form, 'product': product, 'review': review}
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products/"+ str(product.pk))
    else:
        return render(request, 'edit_review.html', context)
