from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class AutoMaker(models.Model):
    name = models.CharField(max_length=16, verbose_name='Automaker name')
    foundation_year = models.IntegerField(default=timezone.now().year,
                                          validators=[MinValueValidator(timezone.now().year - 200),
                                                      MaxValueValidator(timezone.now().year)],
                                          verbose_name='Year of company\'s foundation')
    location = models.CharField(max_length=32, verbose_name='Location of head office')
    comment = models.CharField(max_length=128, null=True, verbose_name='Information about company')
