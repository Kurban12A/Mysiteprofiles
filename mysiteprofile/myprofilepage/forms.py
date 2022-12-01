from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subjects', 'messages']
        widgets = {
            # 'name': forms.TextInput(attrs={'placeholder': 'Your name', 'cols': 60, 'rows': 10}),
            'email': forms.EmailInput(attrs={"autocomplete": "on", 'size': 116.8}),
            # 'messages': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Messages', 'cols': 60, 'rows': 10})
        }
        exclude = ['date_message']


