from django.contrib import admin
from .models import Transaction, TransactionAttachment


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'transaction_type',
        'amount',
        'transaction_date',
        'created_at',
    )

    search_fields = (
        'description',
        'user__username',
        'category__name',
    )

    list_filter = (
        'transaction_type',
        'transaction_date',
        'created_at',
    )

    ordering = (
        '-transaction_date',
        '-created_at',
    )


@admin.register(TransactionAttachment)
class TransactionAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        'transaction',
        'file',
        'uploaded_at',
    )

    list_filter = (
        'uploaded_at',
    )