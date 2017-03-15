# codding: utf-8
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from .models import User


class ModelBackend(BaseModelBackend):

    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        if username:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
