
from .views import (
    LogCreateAPIView,
    LogDeleteAPIView,
    LogDetailAPIView,
    LogListAPIView,
    LogUpdateAPIView, 
    log_excell
)

from django.urls import path
app_name = 'log'

urlpatterns = [
    path('list/', LogListAPIView.as_view(), name='log-list'),
    path('create/', LogCreateAPIView.as_view(), name='log-create'),
    path('<int:pk>/', LogDetailAPIView.as_view(), name="log-detail"),
    path('<int:pk>/edit/', LogUpdateAPIView.as_view(), name="log-edit"),
    path('<int:pk>/delete/', LogDeleteAPIView.as_view(), name="log-delete"),
    path('download/', log_excell, name="log-excell"),

]
