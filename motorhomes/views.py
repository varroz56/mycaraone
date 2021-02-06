from django.shortcuts import render


from .models import Motorhome

from .filters import MotorhomeFilter


from django.contrib import messages

# A view to list all Motorhomes


def MotorhomeListView(request):
    """ This view renders the motorhomes, and if the motorhome filter used
        it will filter the qs too.
     """
    # query every motorhomes
    motorhomes = Motorhome.objects.all()
    # if the filter form was submitted the motofilter will have the new qs for motorhomes to list
    motofilter = MotorhomeFilter(request.GET, queryset=motorhomes)
    # if motofilter qs is empty, so no matching motorhome for the parameters
    # set do not push the result to motorhomes as want to show all motorhomes and show a warning
    motorhorhome_msg = True
    if not motofilter.qs:
        motofilter = MotorhomeFilter()
        messages.add_message(request, messages.WARNING,
                             'No Results for your search, We have reset the Search filters')
    # if there was a match
    else:
        # set motorhomes to the date filtered qs
        # motorhomes = datefilter.qs
        motorhomes = motofilter.qs

        # if only 1 result
        if motorhomes.count() == 1:
            message = "Found " + str(motorhomes.count()) + " Motorhome"
        # if more than 1 result
        else:
            message = "Found " + str(motorhomes.count()) + " Motorhomes"
        messages.add_message(request, messages.SUCCESS,
                             message)

    context = {
        'motorhomes': motorhomes,
        'motofilter': motofilter,
        'motorhorhome_msg': motorhorhome_msg,

    }
    return render(request, 'motorhomes/motorhomes.html', context)


# A View to show details about the chosen motorhome
def MotorhomeDetailedView(request, pk):
    motorhome = Motorhome.objects.get(id=pk)

    context = {
        'motorhome': motorhome,

    }
    return render(request, 'motorhomes/motorhome_details.html', context)
