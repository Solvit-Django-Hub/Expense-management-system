from django.contrib import admin
from .models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'amount',
        'start_date',
        'end_date',
        'created_at',
    )

    search_fields = (
        'user__username',
        'category__name',
    )

    list_filter = (
        'start_date',
        'end_date',
        'created_at',
    )

    ordering = (
        '-start_date',
    )