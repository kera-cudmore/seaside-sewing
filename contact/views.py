from django.shortcuts import render
from .forms import ContactForm
from .models import ContactForm

from django.contrib import messages
from django.conf import settings


def contact(request):
    
    return render(request, 'contact/contact.html')
