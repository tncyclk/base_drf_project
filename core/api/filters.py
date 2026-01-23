from django_filters import rest_framework as filters
from core.models import Log


class LogFilter(filters.FilterSet):
    
    class Meta:
        model = Log
        fields = {
            'created_date': ['lte', 'gte','exact' ],
            'created_time': ['lte', 'gte'],
            'req_url': ['icontains','exact'], 
            'source_ip': ['exact'], 
            'user': ['exact'], 
            'req_type': ['exact'],
            'app_name': ['exact'],
        }