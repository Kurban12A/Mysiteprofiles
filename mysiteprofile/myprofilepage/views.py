from smtplib import SMTPException
from django.conf import settings
from django.core.checks import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect

from .forms import MessageForm


def index_page(request):

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subjects'],
                message=form.cleaned_data['messages'],
                from_email=form.cleaned_data['email'],
                recipient_list=[settings.RECIPIENT_ADDRESS],
                fail_silently=False)
            form.save()
            """return empty form"""
            form = MessageForm()

    context = {'form': form}
    return render(request, 'myprofilepage/index.html', context)


