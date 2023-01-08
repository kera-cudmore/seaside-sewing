from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = (
            'contact_name',
            'contact_email',
            'contact_phone_number',
            'contact_message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_phone_number': 'Phone Number',
            'contact_message': 'Your Message',
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
