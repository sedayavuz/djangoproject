from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
class Executive(models.Model):
     name = models.CharField(max_length=100)
     task = models.CharField(max_length=150)
     mail = models.CharField(max_length=200)
     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
     phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=45) # validators should be a list
