from django.urls import path, include
from django.contrib import admin
admin.autodiscover()

app_name ='core'

urlpatterns = [
    path('log/', include('core.api.urls'), name='log'),
]
