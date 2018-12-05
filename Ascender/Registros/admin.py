from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from .forms import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)