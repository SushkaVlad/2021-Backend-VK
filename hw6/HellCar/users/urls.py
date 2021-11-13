from django.urls import path
from users.views import add_user, show_users, user_detail

urlpatterns = [
    path('add/', add_user, name='add_user'),
    path('show/', show_users, name='show_users'),
    path('inf/<int:user_id>', user_detail, name='user_detail')
]