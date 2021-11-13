from django.urls import path

from cars.views import add_car, show_cars, car_detail, index, update_car, delete_car

urlpatterns = [
    path('add/', add_car, name='add_car'),
    path('show/', show_cars, name='show_cars'),
    path('index/', index, name='index'),
    path('inf/<int:car_id>', car_detail, name='car_detail'),
    path('update/<int:car_id>', update_car, name='update_car'),
    path('delete/<int:car_id>', delete_car, name='delete_car')
]
