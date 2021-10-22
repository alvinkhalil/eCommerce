from django.urls import path
from pages import views

app_name = "pages"

urlpatterns = [ 
    path('',views.index,name="index"),
    path('contactus',views.contactus,name="contactus"),
    path('aboutus',views.aboutus,name = 'about')
    
]
