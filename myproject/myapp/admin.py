from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
# Unregister the provided model admin:
admin.site.unregister(User)