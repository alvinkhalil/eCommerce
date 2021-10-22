from django.urls import path
from products import views
app_name = "products"

urlpatterns = [
    path('category/<slug:category_slug>/<slug:product_slug>/<int:id>',views.product_item, name="product_item"),
    path('all/',views.products_all,name="products_all",)
] 