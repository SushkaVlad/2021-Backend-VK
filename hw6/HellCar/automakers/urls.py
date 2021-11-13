from automakers.views import index, add_maker, show_makers, maker_detail, update_maker, delete_maker
from django.urls import path

urlpatterns = [
    path('add/', add_maker, name='add_maker'),
    path('show/', show_makers, name='show_makers'),
    path('index/', index, name='index'),
    path('inf/<int:maker_id>', maker_detail, name='maker_detail'),
    path('update/<int:maker_id>', update_maker, name='update_maker'),
    path('delete/<int:maker_id>', delete_maker, name='delete_maker')
]
