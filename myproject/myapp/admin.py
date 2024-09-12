from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Person

# Register your models here.

# Unregister the provided model admin:
admin.site.unregister(User)
@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
    
def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs) # override get_form function to disable username field
    is_superuser = request.user.is_superuser
    
    if not is_superuser:
        form.base_fields['username'].disabled = True
        
        return form
    
admin.site.register(Person)