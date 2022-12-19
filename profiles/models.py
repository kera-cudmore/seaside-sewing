from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from django.core.validators import RegexValidator


# need to install countryfield


class UserProfile(models.Model):
    """
    Extends the existing django User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(
        max_length=100,
        blank=False,
    )
    street_address1 = models.CharField(
        max_length=80,
        blank=False,
    )
    street_address2 = models.CharField(
        max_length=80,
        blank=True,
    )
    town_or_city = models.CharField(
        max_length=50,
        blank=False,
    )
    county = models.CharField(
        max_length=80,
        blank=True,
    )
    postcode = models.CharField(
        max_length=20,
        blank=False,
    )
    country = CountryField(
        blank_label='Country',
        null=True,
        blank=False,
    )
    phoneNumberRegex = RegexValidator(
        regex=r"^\+?1?\d{8,15}$",
        message='Please enter a valid phone number',
    )
    phone_number = models.CharField(
        validators=[phoneNumberRegex],
        max_length=16,
        unique=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
