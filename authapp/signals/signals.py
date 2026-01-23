from django.dispatch import receiver
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed
)

from core.create_log import create
from base_drf_project.middlewares.request_middleware import get_current_request


@receiver(user_logged_in)
def user_logged_in_log(sender, request, user, **kwargs):
    request = get_current_request()
    message = f"{user.username} logged in successfully."
    create("Login", message, request)


@receiver(user_logged_out)
def user_logged_out_log(sender, request, user, **kwargs):
    request = get_current_request()
    message = f"{user.username} logged out."
    create("Logout", message, request)
    
@receiver(user_login_failed)
def user_login_failed_log(sender, credentials, request, **kwargs):
    request = get_current_request()
    username = credentials.get("username", "unknown")
    message = f"Failed login attempt for username: {username}"
    create("LoginFailed", message, request)

