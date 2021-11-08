from automakers.models import AutoMaker
from django.db import models
from users.models import User

dict_of_cars = dict()


class Car(models.Model):
    make = models.ForeignKey(AutoMaker, verbose_name='Automaker name', on_delete=models.CASCADE)
    model = models.CharField(max_length=64, verbose_name='Car model')
    type_of_drive = models.CharField(max_length=3, verbose_name='type of wheel drive (4WD, BWD, FWD)')
    price = models.IntegerField(verbose_name='average price of car ($)')
    year = models.CharField(max_length=10,
                            verbose_name='Period of car manufacturing')
    comment = models.CharField(max_length=128, null=True, verbose_name='Information about car')
    creator = models.ForeignKey(User, verbose_name='Topic creator', on_delete=models.CASCADE)
