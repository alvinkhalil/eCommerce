from django.shortcuts import redirect, render
from pages.models import AboutUs, Carousel, CommentCarousel, ContactUsModel, LocationModel
from django.contrib import messages

# Create your views here.
def index(request):
    carousel = Carousel.objects.filter(status = "active")
    comment_car = CommentCarousel.objects.all()
    context = {
        "carousel":carousel,
        "comment_car":comment_car,
    }

    return render(request,"pages/index.html",context)

def contactus(request): 

    locations = LocationModel.objects.filter(status = "active")



    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        neW = ContactUsModel.objects.create(name = name, email = email, subject = subject, message = message)
        neW.save()
        messages.success(request,"Mesajınız uğurla göndərildi.")

        return redirect("pages:contactus")

    context = {
        "locations":locations,
    }
    return render(request,"pages/contactus.html",context)

def aboutus(request):

    about = AboutUs.objects.first()

    context = {
        "about":about,
    }
    
    return render(request,"pages/about.html",context)

