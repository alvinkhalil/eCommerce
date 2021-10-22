from products.models import Product_Category,Product_Item


def categories(request):
    
    categories_all = Product_Category.objects.all()

    context = {
        "categories_all":categories_all,
    }

    return context

def products(request):

    products_slider = Product_Item.objects.filter(status = "active")[:3]

    context = {
        "products_slider":products_slider,
    }

    return context