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
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }
        motorhomes = Motorhome.objects.all()
        form = ContactMessageForm
        context = {
            'motorhomes': motorhomes,
            'contactform': form,
        }
        template = 'home/index.html'
        try:
            # Create and save new ContactUsMessage instance
            message = ContactUsMessage(
                name=form_data['name'],
                email=form_data['email'],
                subject=form_data['subject'],
                message=form_data['message'])
            message.save()
            messages.add_message(request, messages.SUCCESS,
                                 'We saved your message')
            try:
                # setting end and prefix vars
                end = str(message.id)
                prefix = "CMF"
                # in the case of over 9999999 insatnces
                if message.id > 9999999:
                    # backup prefix and the end will roll back to start
                    # from 1
                    prefix = "CMO"
                    end = str(message.id-9999999)
                # get the length of the id
                # fill with 0s while get the required length
                num = len(end)
                mid = ""
                while num < 7:
                    mid += "0"
                    num += 1
                # set ref from the required tags
                ref = prefix + mid + end
            except:
                ref = 'No Reference was created, apologies for the inconvenience'
            try:
                # as Django send_mail required fields
                # name
                name = form_data['name']
                # subject
                subject = ref + " Re: " + form_data['subject']
                # our message
                message = "Dear " + name + ",\n" + "Thank you for contacting MyCaraOne, your enquery reference number: " + \
                    ref + ".\n" + "We will get back to you shortly. \n" + \
                    "Kind Regards, \n" + " MyCaraOne Team"
                # get the email host to set sender
                sender = settings.EMAIL_HOST_USER
                recipient = [form_data['email']]
                send_mail(
                    subject,
                    message,
                    sender,
                    recipient,
                    fail_silently=False
                )
                # message sent successfully
                messages.add_message(request, messages.SUCCESS,
                                     'We have saved your message, please check your email for our response')
                return render(request, template, context)
            except:
                messages.add_message(request, messages.ERROR,
                                     'Sorry, We were unable to send you a response')
                return render(request, template, context)
        except:
            messages.add_message(request, messages.ERROR,
                                 'Sorry, We were unable to save your message')
            return render(request, template, context)
    return render(request, template, context)
