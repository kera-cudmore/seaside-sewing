from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        add aria labels to fields for accessibility
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        self.fields['full_name'].widget.attrs['aria-label'] = 'Full Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Email Address'
        self.fields['phone_number'].widget.attrs['aria-label'] = 'Phone Number'
        self.fields['postcode'].widget.attrs['aria-label'] = 'Post Code'
        self.fields['town_or_city'].widget.attrs['aria-label'] = 'Town or City'
        self.fields['street_address1'].widget.attrs[
            'aria-label'] = 'Street Address 1'
        self.fields['street_address2'].widget.attrs[
            'aria-label'] = 'Street Address 2'
        self.fields['county'].widget.attrs['aria-label'] = 'County'
        self.fields['country'].widget.attrs['aria-label'] = 'Country'

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
