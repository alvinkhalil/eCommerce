from pages.models import LocationModel

def locationmain(request):
    location_main = LocationModel.objects.get(main = True)

    context = {
        "location_main":location_main,
    }   
    return context