from django.shortcuts import redirect, render
from django.contrib import messages
from products.models import Product_Item, Product_Category
from django.core.paginator import Paginator
from taggit.models import Tag

# Create your views here.
def product_item(request,category_slug, product_slug,id):

    category = Product_Category.objects.get(slug = category_slug)
    try:
        product =  Product_Item.objects.get(status = "active",category = category, slug = product_slug, id = id)


        context = {
            "category":category,
            "product":product,
        }
        return render(request,"products/product_item.html",context)

    except:
        
        messages.info(request,"Səhifə aktiv deyil.")
        return redirect("pages:index")

def products_all(request):
    products = Product_Item.objects.filter(status = "active")
    paginator = Paginator(products,5)
    tags= Tag.objects.all()

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        "products":page_obj,
        'tags':tags,
    }
    return render(request,"products/products_list.html",context)

def categories_products(request,category_slug):
    category = Product_Category.objects.get(slug = category_slug)
    products = Product_Item.objects.filter(category = category, status = "active")
    tags= Tag.objects.all()

    paginator = Paginator(products,5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        "products":page_obj,
        'tags':tags,

    }
    return render(request,"products/products_list.html",context)

def tag_products(request,tag):
    products = Product_Item.objects.filter(status = "active", tags__name__in = [tag])
    tags = Tag.objects.all()

    paginator = Paginator(products,5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "products":page_obj,
        'tags':tags,

    }
    return render(request,"products/products_list.html",context)


