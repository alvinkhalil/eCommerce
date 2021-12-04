from django.urls import path
from .views import add_to_card
from card import views
app_name = "card"

urlpatterns = [ 
    path('add_to_card/<slug:slug>',add_to_card, name="add_to_card"),
    path('remote_from_card/<slug:slug>',views.remove_from_card, name="remove_from_card"),
    
]
