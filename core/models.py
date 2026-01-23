from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import json


class Log(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    req_url = models.URLField(max_length=2000, blank=True, null=True)
    source_ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    req_type = models.CharField(max_length=300, null=True, blank=True)
    app_name = models.CharField(max_length=400, blank=True, null=True)
    event = models.CharField(max_length=600, blank=True, null=True)
    message = models.TextField(max_length=5000, blank=True, null=True)
    req_body = models.TextField(null=True, blank=True)

    def set_req_data(self, data):
        self.req_data = json.dumps(data)

    def get_req_data(self):
        return json.loads(self.req_data) if self.req_data else None

    def __str__(self):
        return str(self.created_date)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'created_time', 'req_url', 'message', 'source_ip', 'user', 'req_type', 'event', 'app_name', 'req_body')
    search_fields = ['created_date', 'req_url', 'req_type']
