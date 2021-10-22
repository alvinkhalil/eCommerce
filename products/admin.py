from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from django.contrib import admin

from products.models import Product_Category, Product_Item

# Register your models here.
class ProductItemAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = '{}' height = 50".format(object.image1.url))
    list_display = ["id","name","icon","category","price","stock","status","created_date"]
    list_editable = ["status"]
    list_filter = ["status","created_date","category","stock","price"]
    serach_fields = ["name","category","decsription"]
    list_display_links = ["name"]
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Product_Item,ProductItemAdmin)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Product_Category,ProductCategoryAdmin)