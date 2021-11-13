from cars.models import Car
from users.models import User
from automakers.models import AutoMaker
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def add_car(request):
    try:
        make = AutoMaker.objects.get(name=request.POST.get('make'))
    except AutoMaker.DoesNotExist:
        return HttpResponseBadRequest('Не найдено такого автопроизводителя!')

    try:
        creator = User.objects.get(username=request.POST.get('creator'))
    except User.DoesNotExist:
        return HttpResponseBadRequest('Не найдено такого пользователя!')

    new_car = Car.objects.create(
        make=make,
        model=request.POST.get('model'),
        type_of_drive=request.POST.get('type_of_drive'),
        price=request.POST.get('price'),
        year=request.POST.get('year'),
        comment=request.POST.get('comment'),
        creator=creator)
    return JsonResponse({'status': 'Машина добавлена', 'id': new_car.id})


@require_http_methods(['GET'])
def show_cars(request):
    return JsonResponse({'Список машин': [model_to_dict(car) for car in Car.objects.all()]})


@require_http_methods(['GET'])
def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponseNotFound('Машина не найдена!')
    return JsonResponse(model_to_dict(car))


@require_http_methods(['POST'])
def update_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponseNotFound('Машина не найдена!')

    if 'model' in request.POST:
        car.model = request.POST['model']
    if 'type_of_drive' in request.POST:
        car.type_of_drive = request.POST['type_of_drive']
    if 'price' in request.POST:
        car.price = request.POST['price']
    if 'year' in request.POST:
        car.year = request.POST['year']
    if 'comment' in request.POST:
        car.comment = request.POST['comment']

    car.save()
    return JsonResponse({'status': 'Машина изменена', 'id': car.id})


@require_http_methods(['POST'])
def delete_car(request, car_id):
    try:
        Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponseNotFound('Машина не найдена!')

    Car.objects.filter(id=car_id).delete()
    return JsonResponse({'status': 'Машина удалена', 'id': car_id})


@require_http_methods(['GET'])
def index(request):
    return render(request, 'base.html', context={'header': 'Страница автомобилей'})
