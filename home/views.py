from django.shortcuts import render, redirect
from django.conf import settings
from motorhomes.models import Motorhome
from .forms import ContactMessageForm
from django.core.mail import send_mail
from django.contrib import messages

from django.urls import reverse_lazy


from .models import ContactUsMessage

# index view for the landing page


def IndexView(request):
    motorhomes = Motorhome.objects.all()
    form = ContactMessageForm
    context = {
        'motorhomes': motorhomes,
        'contactform': form,
    }
    return render(request, 'home/index.html', context)


def ContactFormView(request):
    """ Contact Form create a message instance and send a reply email"""
    print('in view')
    if request.method == 'POST':
        print('in post')
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }
        try:
            # Create and save new ContactUsMessage instance
            message = ContactUsMessage(
                name=form_data['email'],
                email=form_data['email'],
                subject=form_data['subject'],
                message=form_data['message'])
            message.save()
            messages.add_message(request, messages.SUCCESS, 'We saved your message')
        except:
            messages.add_message(request, messages.ERROR, 'Sorry, We were unable to save your message')

    return render(request, IndexView)
