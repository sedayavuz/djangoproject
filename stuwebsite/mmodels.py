from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
class Messages(models.Model):
     name = models.CharField(max_length=100)
     tel = models.CharField(max_length=150)
     mail = models.CharField(max_length=200)
     message = models.TextField(default="deger gir")
