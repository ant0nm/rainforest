"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainforest.views import list_products, show_product, root, new_product, create_product, edit_view, edit_product

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('products', list_products, name="products"),
    path('products/<int:id>', show_product, name="show_product"),
    path('new', new_product, name="new_product"),
    path('create', create_product, name="create_product"),
    path('edit_view/<int:id>', edit_view, name="edit_view"),
    path('edited/<int:id>', edit_product, name="edit_product"),
]
