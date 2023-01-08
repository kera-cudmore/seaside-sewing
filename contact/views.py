from django.shortcuts import render, redirect
from .forms import ContactForm
# from .models import ContactForm

from django.contrib import messages
# from django.conf import settings


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your enquiry was sent successfully. \
                Please allow up to 2 working days for a response.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error sending your enquiry. \
            Please ensure all fields are valid and try again.')
            return redirect('contact')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
