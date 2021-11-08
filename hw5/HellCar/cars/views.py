from cars.models import dict_of_cars, Car
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound
# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def add_car(request):
    idx = len(dict_of_cars)
    dict_of_cars[idx] = Car(
        idx,
        request.POST.get('make'),
        request.POST.get('model'),
        request.POST.get('type_of_drive'),
        request.POST.get('price'),
        request.POST.get('year'),
        request.POST.get('comment'))
    return JsonResponse({'status': 'Машина добавлена', 'id': idx})


@require_http_methods(['GET'])
def show_cars(request):
    return JsonResponse({'Список машин': [model_to_dict(car) for car in dict_of_cars.values()]})


@require_http_methods(['GET'])
def car_detail(request, car_id):
    car = dict_of_cars.get(car_id)
    if car is None:
        return HttpResponseNotFound('Нет такой машины')
    return JsonResponse(model_to_dict(car))


@require_http_methods(['GET'])
def index(request):
    return render(request, 'base.html', context={'header': 'Страница автомобилей'})
