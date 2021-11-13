from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseNotFound
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def add_user(request):
    new_user = get_user_model().objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            username=request.POST.get('username'),
    )
    return JsonResponse({'status': 'Пользователь добавлен', 'id': new_user.id})


@require_http_methods(['GET'])
def show_users(request):
    return JsonResponse({'Список пользователей': [dict(
        id=user.id,
        username=user.username) for user in get_user_model().objects.all()]})


@require_http_methods(['GET'])
def user_detail(request, user_id):
    try:
        user = get_user_model().objects.get(id=user_id)
    except get_user_model().DoesNotExist:
        return HttpResponseNotFound('Нет такого пользователя')
    return JsonResponse(dict(
        id=user.id,
        username=user.username,
        email=user.email
    ))
