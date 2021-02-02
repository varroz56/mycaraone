from django.shortcuts import render, redirect, get_object_or_404
from checkout.models import BillingAddress
from .forms import UserProfileUpdateForm, BillingAddressForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView
# A view to show user profile page
from django.conf import settings


def UserProfileView(request):
    profile = request.user.userprofile
    if BillingAddress.objects.filter(user=request.user).exists():
        billingaddress = get_object_or_404(BillingAddress, user=request.user)
    else:
        billingaddress = None
    context = {
        'profile': profile,
        'billingaddress': billingaddress,
    }
    return render(request, 'profiles/myprofile.html', context)

# A view to add or update user profile


def UserProfileUpdateView(request):
    profile = request.user.userprofile
    form = UserProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Unable to update User profile, please try again later')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/update_myprofile.html', context)


# a view to create billing address

def CreateBillingAddressView(request):
    """Billing Address form """

    user = request.user
    template = 'profiles/create_billing_address.html'

    if BillingAddress.objects.filter(user=user):
        messages.add_message(request, messages.ERROR,
                             'Only One Billing Address can be stored on our system')
        return redirect(UserProfileView)
    form = BillingAddress()
    context = {
        'form': form,
        'user': user,
        'api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    print('before post')
    if request.method == 'POST':
        form = BillingAddress()
        print('In post')
        full_name = request.POST.get('full_name', False),
        email = request.POST.get('email', False),
        phone_number = request.POST.get('phone_number', False),
        address_line1 = request.POST.get('street_number', False),
        address_line2 = request.POST.get('route', False),
        postcode = request.POST.get('postal_code', False),
        city = request.POST.get('locality', False),
        country = request.POST.get('country', False),

        print(full_name)
        try:
            billingaddress = BillingAddress(
                user=user,
                full_name=full_name[0],
                email=email[0],
                phone_number=phone_number[0],
                address_line1=address_line1[0],
                address_line2=address_line2[0],
                postcode=postcode[0],
                city=city[0],
                country=country[0],
            )
            billingaddress.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Billing Address added')
        except:
            messages.add_message(request, messages.ERROR,
                                 'Sorry, We were unable to save your Billing Address')
            return render(request, template, context)

    return render(request, template, context)
