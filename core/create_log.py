from core.models import Log
from django.urls import resolve

def create(event, message, request=None):
    
    print("Creating log entry:", event, message)
    app_name = None
    source_ip = None
    req_type = None
    req_url = None
    user = None
    
    if request:
        user = request.user
        source_ip = get_client_ip(request)
        req_type = request.META.get('REQUEST_METHOD')
        req_url = request.build_absolute_uri()
        app_name = resolve(request.path).app_name

    Log.objects.create(
        event=event,
        message=message,
        app_name=app_name,
        user=user,
        req_type=req_type,
        req_url=req_url,
        source_ip=source_ip,
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip