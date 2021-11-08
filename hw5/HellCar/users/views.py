from django.forms import model_to_dict
from users.models import dict_of_users, User
from django.http import JsonResponse, HttpResponseNotFound
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(['POST'])
def add_user(request):
    idx = len(dict_of_users)
    dict_of_users[idx] = User(
        idx,
        request.POST.get('login'),
        request.POST.get('mail'))
    return JsonResponse({'status': 'Пользователь добавлен', 'id': idx})


@require_http_methods(['GET'])
def show_users(request):
    return JsonResponse({'Список пользователей': [model_to_dict(user) for user in dict_of_users.values()]})


@require_http_methods(['GET'])
def user_detail(request, user_id):
    user = dict_of_users.get(user_id)
    if user is None:
        return HttpResponseNotFound('Нет такого пользователя')
    return JsonResponse(model_to_dict(user))
