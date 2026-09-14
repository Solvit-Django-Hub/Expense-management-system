from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'user',
            'name',
            'category_type',
            'description',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
        ]

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                'Category name must contain at least 2 characters.'
            )

        return value

    def validate(self, data):
        user = self.context['request'].user
        name = data.get('name')
        category_type = data.get('category_type')

        queryset = Category.objects.filter(
            user=user,
            name=name,
            category_type=category_type
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                'You already have this category.'
            )

        return data