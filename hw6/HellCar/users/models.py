from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_id': self.id})

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
