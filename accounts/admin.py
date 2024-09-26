from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
    add_fieldsets = (
            (
                None,
                {
                    "fields": (
                        "email",
                        "username",
                        "password1",
                        "password2",
                    ),
                },
            ),
        )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
    )

admin.site.register(get_user_model(), CustomUserAdmin)