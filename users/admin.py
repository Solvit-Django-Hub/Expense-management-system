from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'email',
        'phone_number',
        'dob',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'full_name',
        'email',
        'phone_number',
        'user__username',
    )

    list_filter = (
        'created_at',
        'updated_at',
    )
    