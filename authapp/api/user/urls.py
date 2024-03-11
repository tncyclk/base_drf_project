from django.urls import path
from .views import (
    all_users_list
)

app_name = 'users'

urlpatterns = [
    path('all_users/', all_users_list ,name="all-list"),
]
