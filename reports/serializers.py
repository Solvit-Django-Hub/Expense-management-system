from rest_framework import serializers
from .models import Budget
from categories.serializers import CategorySerializer


class BudgetSerializer(serializers.ModelSerializer):

    category_details = CategorySerializer(
        source='category',
        read_only=True
    )

    class Meta:
        model = Budget
        fields = [
            'id',
            'user',
            'category',
            'category_details',
            'amount',
            'start_date',
            'end_date',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'category_details',
            'created_at',
            'updated_at',
        ]

    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                'Budget amount must be greater than zero.'
            )

        return value

    def validate(self, data):

        start_date = data.get(
            'start_date',
            self.instance.start_date if self.instance else None
        )

        end_date = data.get(
            'end_date',
            self.instance.end_date if self.instance else None
        )

        category = data.get(
            'category',
            self.instance.category if self.instance else None
        )

        if start_date and end_date:

            if start_date >= end_date:
                raise serializers.ValidationError(
                    'Start date must be before end date.'
                )

        if category:

            if category.category_type != 'EXPENSE':
                raise serializers.ValidationError(
                    'A budget can only be created for an expense category.'
                )

        request = self.context.get('request')

        if request and request.user.is_authenticated and category:

            if category.user != request.user:
                raise serializers.ValidationError(
                    'You can only use your own categories.'
                )

        return data