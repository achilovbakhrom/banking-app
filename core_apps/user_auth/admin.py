from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserCreationForm, UserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "role",
        "account_status",
    ]
    list_filter = ["email", "role", "is_staff", "is_active"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("username", "email", "password")}),
        (
            _("Personal Information"),
            {"fields": ("first_name", "middle_name", "last_name", "id_no", "role")},
        ),
        (
            _("Security"),
            {"fields": ("security_question", "security_answer", "otp", "otp_expiry")},
        ),
        (
            _("Account Status"),
            {
                "fields": (
                    "account_status",
                    "failed_login_attempts",
                    "last_failed_login",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ["email", "username", "first_name", "last_name", "id_no"]
    ordering = ["email"]
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": (
    #                 "email",
    #                 "id_no",
    #                 "first_name",
    #                 "last_name",
    #                 "security_question",
    #                 "security_answer",
    #                 "role",
    #                 "account_status",
    #                 "is_staff",
    #                 "is_active",
    #                 "password1",
    #                 "password2",
    #             ),
    #         },
    #     ),
    # )
