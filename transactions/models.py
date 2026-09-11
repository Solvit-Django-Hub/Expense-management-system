from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='transactions')
    transaction_type = models.CharField( max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField( max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField( blank=True, null=True)
    transaction_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-transaction_date', '-created_at']

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"


class TransactionAttachment(models.Model):

    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='transaction_receipts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.transaction}"