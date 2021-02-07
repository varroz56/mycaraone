from django.shortcuts import render, redirect, reverse, get_object_or_404
from checkout.models import BillingAddress
from .forms import UserProfileUpdateForm, BillingAddressForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView
# A view to show user profile page
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
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


@login_required
def UserProfileUpdateView(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            UserProfile.objects.filter(user=request.user).update(
                phone_number=form.data['phone'],
                profile_picture=form.data['profile_picture']
            )
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse(UserProfileView))
        else:
            messages.error(
                request, 'Unable to update User profile, please try again later')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/update_myprofile.html', context)


# a view to create billing address
@login_required
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
    }

    if request.method == 'POST':
        form = BillingAddress()
        full_name = request.POST.get('full_name', False),
        email = request.POST.get('email', False),
        phone_number = request.POST.get('phone_number', False),
        address_line1 = request.POST.get('street_number', False),
        address_line2 = request.POST.get('route', False),
        postcode = request.POST.get('postal_code', False),
        city = request.POST.get('locality', False),
        country = request.POST.get('country', False),

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
                                 'Billing Address added successfully')
            return redirect(reverse(UserProfileView))
        except:
            messages.add_message(request, messages.ERROR,
                                 'Sorry, We were unable to save your Billing Address')
            return render(request, template, context)

    return render(request, template, context)


@login_required
def UpadeBillingAddressView(request):
    """Billing Address form """
    user = request.user
    template = 'profiles/update_billing_address.html'

    if not BillingAddress.objects.filter(user=user):
        messages.add_message(request, messages.ERROR,
                             'You have not added Billing Address yet, please add first')
        return redirect(CreateBillingAddressView)

    addr = get_object_or_404(BillingAddress, user=request.user)

    form = BillingAddress()
    context = {
        'form': form,
        'user': user,
        'addr': addr,
    }

    if request.method == 'POST':
        form = BillingAddress()
        full_name = request.POST.get('full_name', False),
        email = request.POST.get('email', False),
        phone_number = request.POST.get('phone_number', False),
        address_line1 = request.POST.get('street_number', False),
        address_line2 = request.POST.get('route', False),
        postcode = request.POST.get('postal_code', False),
        city = request.POST.get('locality', False),
        country = request.POST.get('country', False),

        try:
            BillingAddress.objects.filter(id=addr.id).update(
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

            messages.add_message(request, messages.SUCCESS,
                                 'Successfully updated your Billing address')
            return redirect(reverse(UserProfileView))
        except:
            messages.add_message(request, messages.ERROR,
                                 'Sorry, We were unable to update your Billing Address')
            return render(request, template, context)

    return render(request, template, context)


# a view to confirm billing address deletion
@login_required
def ConfirmDeleteBillingAddressView(request):
    return render(request, 'profiles/confirm_delete_billing_address.html')


# a view to delete billing address
@login_required
def DeleteBillingAddressView(request):
    user = request.user

    if not BillingAddress.objects.filter(user=user):
        messages.add_message(request, messages.WARNING,
                             'You have no saved Billing Address at the moment')
        return redirect(UserProfileView)

    try:
        addr = get_object_or_404(BillingAddress, user=user)
        addr.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Billing Address has been deleted')
        return redirect(UserProfileView)
    except:
        messages.add_message(request, messages.ERROR,
                             'Unable to delete Billing Address, please try again later or contact us')
        return redirect(UserProfileView)
