from django.urls import path, include
from django.contrib import admin

from rest_framework.authtoken import views
from django.contrib.auth import views as auth_views
from .views import logout

admin.autodiscover()

app_name = 'auth_app'


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', logout, name="logout"),
    path('users/', include('authapp.api.user.urls'), name="users")
]