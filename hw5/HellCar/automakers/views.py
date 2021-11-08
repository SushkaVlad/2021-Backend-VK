from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def index(request):
    return render(request, 'base.html', context={'header': 'Страница марок автомобилей'})
