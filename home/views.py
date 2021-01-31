from django.shortcuts import render
from motorhomes.models import Motorhome


# index view for the landing page
def IndexView(request):
    motorhomes=Motorhome.objects.all()

    context={
        'motorhomes':motorhomes,
    }
    return render(request, 'home/index.html', context)
