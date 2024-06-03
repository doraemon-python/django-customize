from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import User

admin.site.register(User)
admin.site.register(Session)
