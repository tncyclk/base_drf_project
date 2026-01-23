from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view
from .filters import LogFilter
from .serializers import LogSerializer
from core.models import Log

import io
import xlsxwriter
from datetime import datetime
from django.http import HttpResponse
class LogCreateAPIView(CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogListAPIView(ListAPIView):  
    queryset = Log.objects.all()
    serializer_class = LogSerializer  
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LogFilter

class LogDetailAPIView(RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogDeleteAPIView(DestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    
    
@api_view(['POST'])
def log_excell(request):
    query = request.data.get('logs')
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    header_style = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter',"font_color": "#666699","bg_color": "#f2f2f2"})
    row_style = workbook.add_format({'align': 'center', 'valign': 'vcenter',"text_wrap": True})
    headers = ['Created Date', 'Message', 'Source IP', 'User', 'Requirement Type', 'App Name']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header, header_style)
        worksheet.set_column(0, 0, 10)
        worksheet.set_column(1, 1, 40)
        worksheet.set_column(2, 2, 15)
        worksheet.set_column(3, 3, 10)
        worksheet.set_column(4, 4, 15)
        worksheet.set_column(5, 5, 25)

    for row_num, obj in enumerate(query):
        worksheet.write(row_num + 2, 0, obj.get('created_date'), row_style)
       
        worksheet.write(row_num + 2, 1, obj.get('message'), row_style)
        
        worksheet.write(row_num + 2, 2, obj.get('source_ip'), row_style)
        
        worksheet.write(row_num + 2, 3, obj.get('user'), row_style)
        
        worksheet.write(row_num + 2, 4, obj.get('req_type'), row_style)
        
        worksheet.write(row_num + 2, 5, obj.get('app_name'), row_style)

    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(),content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Logs' + \
        str(datetime.now())+'.xlsx'

    output.close()

    return response
  