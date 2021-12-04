from django.contrib import admin

from card.models import Order, OrderItem

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Order)