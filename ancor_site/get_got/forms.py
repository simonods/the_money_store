from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from .models import *


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_("Username"), max_length=150)
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)
    # make cheecbox for REMEMBER ME

    class Meta:
        model = UserInfo
        fields = ['username', 'password',]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), required=True)
    phone_number = forms.CharField(label=_("Phone number"), max_length=20, required=False)
    country = CountryField().formfield(label=_("Country/Region"), empty_label='Choose country', required=False)
    address = forms.CharField(label=_("Shipping address"), max_length=255, required=False)
    date_of_birth = forms.DateField(label=_("Date of birth"), required=False,
                                    widget=forms.DateInput(attrs={'type': 'date'}))
    gender_choices = [
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other')),
        ('mechanic', _('Mechanic'))
    ]
    gender = forms.ChoiceField(label=_("Gender"), choices=gender_choices, required=False)
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Repeat password"), widget=forms.PasswordInput)

    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['country'].empty_label = 'Choose country'

        model = UserInfo
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'country', 'address', 'date_of_birth',
                  'gender']


class ForgotPassword(ModelForm):
    username = forms.CharField(label=_("Username"), max_length=150)
    email = forms.EmailField(label=_("Email"), required=True)

    class Meta:
        model = UserInfo
        fields = ['username', 'email',]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['image', 'title']
