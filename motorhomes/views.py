from django.shortcuts import render


from .models import Motorhome

from .filters import MotorhomeFilter


# A view to list all Motorhomes
def MotorhomeListView(request):
    """ This view renders the motorhomes, and if the motorhome filter used 
        it will filter the qs too.
     """
    motorhomes = Motorhome.objects.all()
    print('initial')
    print( motorhomes)
    motofilter = MotorhomeFilter(request.GET, queryset=motorhomes)
    print('motofilter')
    print(motofilter.qs)
    motorhomes = motofilter.qs
    print('passing qs')
    print(motorhomes)
    context = {
        'motorhomes': motorhomes,
        'motofilter': motofilter,
    }
    return render(request, 'motorhomes/motorhomes.html', context)


# A View to show details about the chosen motorhome
def MotorhomeDetailedView(request, pk):
    motorhome = Motorhome.objects.get(id=pk)

    context = {
        'motorhome': motorhome,

    }
    return render(request, 'motorhomes/motorhome_details.html', context)
