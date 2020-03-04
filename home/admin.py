from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Customer, Order
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms


admin.site.register(Customer)

class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label="E-mail", max_length=75)


UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2', 'groups', 'is_active')
    }),
)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)