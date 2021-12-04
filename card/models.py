from django.db import models
from django.db.models.deletion import CASCADE
from products.models import Product_Item
from django.conf import settings
# Create your models here.
class OrderItem(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE)
    item = models.ForeignKey(Product_Item,on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.quantity} ədəd {self.item} məhsuldan"

class Order(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    started_date = models.DateTimeField(auto_now_add=True)
    ordered_date =models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
