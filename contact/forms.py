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
        Add placeholders,
        remove auto-generated labels
        set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_phone_number': 'Phone Number',
            'contact_message': 'Your Message',
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True
        self.fields['contact_name'].widget.attrs['aria-label'] = 'Contact name'
        self.fields['contact_email'].widget.attrs[
            'aria-label'] = 'Email'
        self.fields['contact_phone_number'].widget.attrs[
            'aria-label'] = 'Phone number'
        self.fields['contact_message'].widget.attrs[
            'aria-label'] = 'Your message'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
