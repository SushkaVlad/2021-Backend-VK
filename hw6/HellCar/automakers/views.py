from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from automakers.models import AutoMaker


@require_http_methods(['POST'])
def add_maker(request):
    new_maker = AutoMaker.objects.create(
        name=request.POST.get('name'),
        foundation_year=request.POST.get('foundation_year'),
        location=request.POST.get('location'),
        comment=request.POST.get('comment'))
    return JsonResponse({'status': 'Автопроизводитель добавлен', 'id': new_maker.id})


@require_http_methods(['GET'])
def show_makers(request):
    return JsonResponse({'Список автопроизводителей': [model_to_dict(maker) for maker in AutoMaker.objects.all()]})


@require_http_methods(['GET'])
def maker_detail(request, maker_id):
    try:
        maker = AutoMaker.objects.get(id=maker_id)
    except AutoMaker.DoesNotExist:
        return HttpResponseNotFound('Марка машины не найдена!')
    return JsonResponse(model_to_dict(maker))


@require_http_methods(['POST'])
def update_maker(request, maker_id):
    try:
        maker = AutoMaker.objects.get(id=maker_id)
    except AutoMaker.DoesNotExist:
        return HttpResponseNotFound('Автопроизводитель не найден!')

    if 'name' in request.POST:
        maker.name = request.POST['name']
    if 'foundation_year' in request.POST:
        maker.foundation_year = request.POST['foundation_year']
    if 'location' in request.POST:
        maker.location = request.POST['location']
    if 'comment' in request.POST:
        maker.comment = request.POST['comment']

    maker.save()
    return JsonResponse({'status': 'Автопроизводитель изменен', 'id': maker.id})


@require_http_methods(['POST'])
def delete_maker(request, maker_id):
    try:
        AutoMaker.objects.get(id=maker_id)
    except AutoMaker.DoesNotExist:
        return HttpResponseNotFound('Автопроизводитель не найден!')

    AutoMaker.objects.filter(id=maker_id).delete()
    return JsonResponse({'status': 'Автопроизводитель удален', 'id': maker_id})


@require_http_methods(['GET'])
def index(request):
    return render(request, 'base.html', context={'header': 'Страница марок автомобилей'})
