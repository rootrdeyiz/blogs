from django.contrib.auth import get_user

def user(request):
    return {
        'current_user': get_user(request)
    }
