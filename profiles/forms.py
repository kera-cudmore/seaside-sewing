from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field,
        add aria labels to fields for accessibility
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        self.fields['default_full_name'].widget.attrs[
            'aria-label'] = 'Full Name'
        self.fields['default_street_address2'].widget.attrs[
            'aria-label'] = 'Street Address 1'
        self.fields['default_street_address1'].widget.attrs[
            'aria-label'] = 'Street Address 2'
        self.fields['default_town_or_city'].widget.attrs[
            'aria-label'] = 'Town or City'
        self.fields['default_county'].widget.attrs[
            'aria-label'] = 'County, State or Locality'
        self.fields['default_postcode'].widget.attrs[
            'aria-label'] = 'Post Code'
        self.fields['default_phone_number'].widget.attrs[
            'aria-label'] = 'Phone Number'
        self.fields['default_country'].widget.attrs['aria-label'] = 'Country'

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'profile-form-input')
            self.fields[field].label = False
