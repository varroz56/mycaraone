from django.forms import ModelForm
from .models import ContactUsMessage


class ContactMessageForm(ModelForm):
    """ Define used model and fields, then
        set placeholder and customzie form fields further """
    class Meta:
        model = ContactUsMessage
        exclude = ['reference']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Type Your Message Here ',
        }
        for field in self.fields:
            placeholder = f"{placeholders[field]} *"
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = "contactform-field py-1 my-1 rounded"
            self.fields[field].widget.attrs['placeholder'] = placeholder
