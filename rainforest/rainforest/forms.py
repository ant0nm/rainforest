from django.forms import ModelForm
from rainforest.models import Product, Review

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
