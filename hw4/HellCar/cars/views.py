from cars.models import dict_of_cars, Car
from django.http import JsonResponse, HttpResponseNotFound
# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def add_car(request):
    idx = len(dict_of_cars)
    dict_of_cars[idx] = Car(
        idx,
        request.POST.get('model'),
        request.POST.get('price'),
        request.POST.get('comment'))
    return JsonResponse({'status': 'Машина добавлена', 'id': idx})


@require_http_methods(['GET'])
def show_cars(request):
    return JsonResponse({'Список машин': [car.__dict__ for car in dict_of_cars.values()]})


@require_http_methods(['GET'])
def car_detail(request, car_id):
    car = dict_of_cars.get(car_id)
    if car is None:
        return HttpResponseNotFound('Нет такой машины')
    return JsonResponse(car.__dict__)


@require_http_methods(['GET'])
def index(request):
    return render(request, 'base.html', context={'header': 'Страница автомобилей'})
