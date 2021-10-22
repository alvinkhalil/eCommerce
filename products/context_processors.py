from products.models import Product_Category


def categories(request):
    
    categories_all = Product_Category.objects.all()

    context = {
        "categories_all":categories_all,
    }

    return context