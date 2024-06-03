from uuid import uuid4

from django.db import models

USERNAME_MAX_LENGTH = 32


class UserManager(models.Manager):
    # Required for login to admin site with username and password
    def get_by_natural_key(self, username: str):
        return self.get(username=username)

    # Required for creating superuser
    def create_superuser(self, username: str):
        return self.create(username=username)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True)

    def __str__(self) -> str:
        return self.username

    # Required for setting as AUTH_USER_MODEL
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"
    is_anonymous = False
    is_authenticated = True

    # Required for using the admin site
    is_active = True
    is_staff = True

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def has_perm(self, perm: str, obj=None) -> bool:
        return True

    def get_username(self):
        return self.username

    # Required for login to admin site with username and password
    manager = UserManager()

    def set_password(self, raw_password: str):
        pass

    def check_password(self, raw_password: str) -> bool:
        return False
