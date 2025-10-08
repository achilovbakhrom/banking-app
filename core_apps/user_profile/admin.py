from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Profile, NextOfKin


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class NextOfKinInline(admin.TabularInline):
    model = NextOfKin
    extra = 1
    fields = ("first_name", "last_name", "relationship", "phone_number", "is_primary")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = (
        "user",
        "full_name",
        "phone_number",
        "email",
        "employment_status",
        "country",
        "view_next_of_kin",
    )
    list_display_links = ("user",)
    list_filter = ("gender", "marital_status", "employment_status", "country")
    search_fields = (
        "user__email",
        "user__last_name",
        "user__last_name",
        "phone_number",
    )
    readonly_fields = ("user",)
    fieldsets = (
        (
            _("Personal Information"),
            {
                "fields": (
                    "user",
                    "title",
                    "gender",
                    "date_of_birth",
                    "marital_status",
                )
            },
        ),
        (
            _("Contact Information"),
            {
                "fields": (
                    "phone_number",
                    "address",
                    "city",
                    "country",
                )
            },
        ),
        (
            _("Identification"),
            {
                "fields": (
                    "means_of_identification",
                    "id_issued_date",
                    "id_expiry_date",
                    "passport_number",
                )
            },
        ),
        (
            _("Employment Information"),
            {
                "fields": (
                    "employment_status",
                    "employer_name",
                    "annual_income",
                    "date_of_employment",
                    "employer_address",
                    "employer_state",
                )
            },
        ),
    )
    inlines = [NextOfKinInline]

    def full_name(self, obj):
        return obj.user.full_name

    full_name.short_description = _("Full Name")

    def email(self, obj):
        return obj.user.email

    email.short_description = _("Email")

    def view_next_of_kin(self, obj):
        count = obj.next_of_kin.count()
        return format_html(
            '<a href="/admin/core_apps/user_profile/nextofkin/?profile__id__exact={}">{} Next of Kin</a>',
            obj.id,
            count,
        )

    view_next_of_kin.short_description = _("Next of Kin")


@admin.register(NextOfKin)
class NextOfKinAdmin(admin.ModelAdmin):
    list_display = ("full_name", "relationship", "profile", "is_primary")
    list_filter = (
        "is_primary",
        "relationship",
    )
    search_fields = ("first_name", "last_name", "profile__user__email")
    readonly_fields = ("profile",)

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = _("Full Name")
