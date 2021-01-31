from django.shortcuts import render
from checkout.models import BillingAddress
from .forms import UserProfileUpdateForm, BillingAddressForm
# A view to show user profile page


def UserProfileView(request):
    profile = request.user.userprofile
    if BillingAddress.objects.filter(user=request.user).exists():
        billingaddress = BillingAddress.objects.get(user=request.user)
    else:
        billingaddress = None
    context = {
        'profile': profile,
        'billingaddress': billingaddress,
    }
    return render(request, 'profiles/myprofile.html', context)


def UserProfileUpdateView(request):
    profile = request.user.userprofile
    form = UserProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/update_myprofile.html', context)
