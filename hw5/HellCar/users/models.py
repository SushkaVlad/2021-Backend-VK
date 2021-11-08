from django.db import models

dict_of_users = dict()


class User(models.Model):
    login = models.CharField(max_length=32, verbose_name='User login')
    email = models.EmailField(max_length=32, verbose_name='User\'s mail')
    # password
