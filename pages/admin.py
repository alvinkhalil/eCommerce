from django.contrib import admin

from pages.models import AboutUs, Carousel, ContactUsModel, LocationModel

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

admin.site.register(Carousel)

