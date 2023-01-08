from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_message',
        'date',
    )

    fields = (
        'contact_email',
        'date',
        'contact_name',
        'contact_phone_number',
        'contact_message',
        'replied',
    )

    list_display = (
        'contact_email',
        'date',
        'replied',
    )

    ordering = ('-date',)


admin.site.register(ContactForm, ContactFormAdmin)
