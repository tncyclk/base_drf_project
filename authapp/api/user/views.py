from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import JsonResponse

@api_view(['GET'])
def all_users_list(request):
    all_users = User.objects.all()
    serializer = UserSerializer(data=all_users, many=True)
    serializer.is_valid()
    return JsonResponse({
        'users': serializer.data
    })