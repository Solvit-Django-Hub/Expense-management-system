from rest_framework import serializers
from .models import Transaction, TransactionAttachment
from categories.serializers import CategorySerializer


class TransactionAttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionAttachment
        fields = [
            'id',
            'transaction',
            'file',
            'uploaded_at',
        ]

        read_only_fields = [
            'id',
            'uploaded_at',
        ]


class TransactionSerializer(serializers.ModelSerializer):

    category_details = CategorySerializer(
        source='category',
        read_only=True
    )

    attachments = TransactionAttachmentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'category',
            'category_details',
            'transaction_type',
            'amount',
            'description',
            'transaction_date',
            'attachments',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'category_details',
            'attachments',
            'created_at',
            'updated_at',
        ]

    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                'Amount must be greater than zero.'
            )

        return value

    def validate(self, data):

        transaction_type = data.get(
            'transaction_type',
            self.instance.transaction_type if self.instance else None
        )

        category = data.get(
            'category',
            self.instance.category if self.instance else None
        )

        if transaction_type and category:

            if transaction_type != category.category_type:
                raise serializers.ValidationError(
                    'Transaction type must match the category type.'
                )

        request = self.context.get('request')

        if request and request.user.is_authenticated and category:

            if category.user != request.user:
                raise serializers.ValidationError(
                    'You can only use your own categories.'
                )

        return data