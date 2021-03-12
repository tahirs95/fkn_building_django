from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactUs(UserCreationForm):
    contact_name = forms.CharField(max_length=250, required=True)
    contact_email = forms.EmailField(max_length=100, required=True)
   # contact_mobile = PhoneField(blank=True, help_text='Contact phone number')
    contact_mobile = forms.EmailField(max_length=15, required=True)
    contact_message = forms.Textarea()
