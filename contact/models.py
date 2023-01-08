from django.db import models


class ContactForm(models.Model):
    contact_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    contact_email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    contact_phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    contact_message = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    replied = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.contact_email
