import phonenumbers
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.title[:25]}..."


def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError('Invalid phone number')
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError('Invalid phone number format')


class UserInfo(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=20, validators=[validate_phone_number], blank=True, null=True)

    country = CountryField(_('country/region'), blank=True, null=True)
    address = models.CharField(_('shipping address'), max_length=255, blank=True, null=True)

    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)

    gender_choices = [
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other')),
        ('mechanic', _('Mechanic'))
    ]
    gender = models.CharField(_('gender'), max_length=10, choices=gender_choices, blank=True, null=True)

    usd_balance = models.DecimalField(_('USD balance'), max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_usd_balance = models.DecimalField(_('Bonus USD balance'), max_digits=10, decimal_places=2, blank=True, null=True)

    verification_image = models.ImageField(_('verification image'), upload_to='verification/%Y/%m/%d/', null=True, blank=True)
    verification_accepted = models.BooleanField(_('is verified'), default=False)

    bottomless_pit = models.BooleanField(_('bottomless pit'), default=False)

    registration_date = models.DateTimeField(_('registration date'), auto_now_add=True)
    last_action_date = models.DateTimeField(_('last action date'), auto_now=True)
    last_session_date = models.DateTimeField(_('last session date'), blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Cryptanu')
        verbose_name_plural = _('Cryptanu')
        ordering = ['last_action_date', 'username']
        swappable = 'AUTH_USER_MODEL'


# UserInfo._meta.get_field('groups').related_name = 'user_groups'
# UserInfo._meta.get_field('user_permissions').related_name = 'user_permissions'

