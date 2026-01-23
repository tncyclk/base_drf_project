from rest_framework.serializers import ModelSerializer, DateTimeField
from core.models import Log
from core import constants


class LogSerializer(ModelSerializer):
    created_date=DateTimeField(format=constants.DATE_FORMAT,required=False)
    class Meta: 
        model = Log
        fields = (
            'id',
            'created_date',
            'created_time',
            'req_url',
            'source_ip',
            'user',
            'req_type',
            'app_name',
            'event',
            'message',
            'req_body'
        )

class LogCreateSerializer(ModelSerializer):
    created_date=DateTimeField(format=constants.DATE_FORMAT,required=False)
    class Meta: 
        model = Log
        fields = (
            'id',
            'created_date',
            'created_time',
            'req_url',
            'source_ip',
            'user',
            'req_type',
            'app_name',
            'event',
            'message',
            'req_body'
        )
