from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category_type',
        'user',
        'created_at',
    )

    search_fields = (
        'name',
        'description',
        'user__username',
    )

    list_filter = (
        'category_type',
        'created_at',
    )