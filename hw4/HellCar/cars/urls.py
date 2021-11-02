from django.urls import path

from cars.views import add_car, show_cars, car_detail, index

urlpatterns = [
    path('add/', add_car, name='add_car'),
    path('show/', show_cars, name='show_cars'),
    path('index/', index, name='index'),
    path('inf/<int:car_id>', car_detail, name='car_detail')
]
