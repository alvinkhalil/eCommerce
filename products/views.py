from django.shortcuts import render
from django.contrib import messages
from products.models import Product_Item, Product_Category
# Create your views here.
def product_item(request,category_slug, product_slug,id):

    category = Product_Category.objects.get(slug = category_slug)
    product =  Product_Item.objects.get(category = category, slug = product_slug, id = id)


    context = {
        "category":category,
        "product":product,
    }
    return render(request,"products/product_item.html",context)
