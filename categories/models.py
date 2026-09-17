from django.db import models
from django.conf import settings


class Category(models.Model):

    CATEGORY_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    category_type = models.CharField( max_length=10,choices= CATEGORY_TYPES )
    description = models.TextField( blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.name} - {self.category_type}"

    