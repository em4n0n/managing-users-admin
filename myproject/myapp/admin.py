from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Unregister the provided model admin:

admin.site.unregister(User)
@admin.register(User)
class NewAdmin(UserAdmin):
    pass