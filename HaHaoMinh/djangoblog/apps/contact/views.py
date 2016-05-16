from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context

# from .models import Contact
from .forms import ContactForm


# Create your views here.
def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            content = "From: %s.\nMessage: %s" % (from_email, message)
            email = EmailMessage(subject, content, to=['minhhahao@gmail.com'])
            email.send()
            messages.success(request, "Sending contact success!")
            return render(request, 'contact_form_sent.html')
        else:
            messages.error(request, "Sending contact fail!")
    else:
        form = ContactForm()

    return render(request, "contact_form.html", {
        'form': form,
    })


def contact_form_sent(request):
    return render(request, 'contact_form_sent.html')
