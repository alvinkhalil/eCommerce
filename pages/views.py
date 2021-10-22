from django.shortcuts import redirect, render
from pages.models import AboutUs, ContactUsModel, LocationModel
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request,"pages/index.html")

def contactus(request): 

    locations = LocationModel.objects.all()



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