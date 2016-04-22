from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        name = form.cleaned_data.get("name")
        message = form.cleaned_data.get("message")

        subject = 'DJANGO'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['djangolalalalala@gmail.com']

        contact_message = "%s: %s via %s" % (name, message, email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('contact')
    context = {'form': form}
    return render(request, 'contact.html', context)


