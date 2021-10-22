from django.contrib import admin
from django.utils.html import format_html

from pages.models import AboutUs, Carousel, CommentCarousel, ContactUsModel, LocationModel

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name","subject","email","status","created_date"]
    list_filter = ["status","created_date","subject"]
    search_fields = ["name","message","email","subject"]
    list_editable = ["status"]

admin.site.register(ContactUsModel,ContactUsAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ["name","status","created_date"]
    list_editable = ["status"]

admin.site.register(LocationModel,LocationAdmin)
admin.site.register(AboutUs)

class CarouselAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = '{}' height = 60 width = 80 style = 'border-radius: 20px;' ".format(object.image.url))

    list_display = ["title","icon","status","is_show","is_show2","created_date"]
    list_editable =["status","is_show","is_show2"]


admin.site.register(Carousel,CarouselAdmin)

class CommenCarouselAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = '{}' height = 50  style = 'border-radius: 20px;' ".format(object.image.url))
    list_display = ["name","icon","job","created_date"]

admin.site.register(CommentCarousel,CommenCarouselAdmin)
    