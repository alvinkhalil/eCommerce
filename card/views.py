from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product_Item
from .models import OrderItem,Order
from django.contrib import messages
from django.utils import timezone
# Create your views here.

def add_to_card(request,slug):
    item = get_object_or_404(Product_Item, slug = slug)
    order_item, created = OrderItem.objects.get_or_create(user = request.user, item = item, ordered =False)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    #Səbətin olub olmadığını yoxlayıram
    if order_qs:
        order = order_qs[0]
        #Eyni məhsuldan olub olmadığını yoxlayıram
        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        
        else:
            order.items.add(order_item)
    else:
        date = timezone.now()
        order = Order.objects.create(user = request.user, ordered_date = date)
        order.items.add(order_item)
        
    messages.success(request,"Səbətə əlavə olundu.")
    return redirect("pages:index")
        
        
def remove_from_card(request,slug):
    item = get_object_or_404(Product_Item, slug = slug)
    order_qs = Order.objects.filter(user = request.user, ordered = False)

    if order_qs:
        order = order_qs[0]
        if order.items.filter(item__slug = slug).exists():
            order_item = OrderItem.objects.filter(item = item, ordered =False, user = request.user)[0]

            order.items.remove(order_item)
            messages.success(request,"Məhsul səbətdən uğurla silindi")
        else:
            messages.info(request,"Bu məhsuldan səbətdə yoxdur")
    else:
        messages.info(request,"Sizin səbətiniz boşdur")

    return redirect("pages:index")