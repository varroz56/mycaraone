from django.shortcuts import render


from .models import Motorhome


# A view to list all Motorhomes
def MotorhomeListView(request):
    motorhomes = Motorhome.objects.all()
    context = {
        'motorhomes': motorhomes}
    return render(request, 'motorhomes/motorhomes.html', context)


# A View to show details about the chosen motorhome
def MotorhomeDetailedView(request, pk):
    motorhome=Motorhome.objects.get(id=pk)

    context={
        'motorhome': motorhome,
    }
    return render(request, 'motorhomes/motorhome_details.html', context)
