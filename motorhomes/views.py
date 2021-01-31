from django.shortcuts import render


from .models import Motorhome


# A view to list all Motorhomes
def MotorhomeListView(request):
    motorhomes = Motorhome.objects.all()
    context = {
        'motorhomes': motorhomes}
    return render(request, 'motorhomes/motorhomes.html', context)
