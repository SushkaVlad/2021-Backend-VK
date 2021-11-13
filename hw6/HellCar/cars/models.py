from automakers.models import AutoMaker
from django.conf import settings
from django.db import models
from django.urls import reverse


class Car(models.Model):
    OPT_OF_DRIVES = [
        ('4WD', 'Four-wheel drive'),
        ('RWD', 'Rear-wheel drive'),
        ('FWD', 'Front-wheel drive'),
    ]
    make = models.ForeignKey(AutoMaker, verbose_name='Automaker name', on_delete=models.CASCADE)
    model = models.CharField(max_length=64, verbose_name='Car model')
    type_of_drive = models.CharField(max_length=3, choices=OPT_OF_DRIVES,
                                     verbose_name='type of wheel drive (4WD, RWD, FWD)')
    price = models.FloatField(verbose_name='average price of car ($)')
    year = models.CharField(max_length=10,
                            verbose_name='Period of car manufacturing')
    comment = models.CharField(max_length=128, null=True, blank=True, verbose_name='Information about car')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Topic creator', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id': self.id})

    def __str__(self):
        return "{} {}".format(self.make, self.model)

    class Meta:
        ordering = ['make']
        db_table = 'cars'
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
