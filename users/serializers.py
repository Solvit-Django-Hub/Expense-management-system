from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'full_name',
            'email',
            'phone_number',
            'dob',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]

    def validate_full_name(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                'Full name must contain at least 2 characters.'
            )

        return value

    def validate_phone_number(self, value):
        value = value.strip()

        if not value.startswith('+250'):
            raise serializers.ValidationError(
                'Phone number must start with +250.'
            )

        if not value[4:].isdigit():
            raise serializers.ValidationError(
                'Phone number must contain only digits after +250.'
            )

        if len(value) != 13:
            raise serializers.ValidationError(
                'Phone number must be in the format +250XXXXXXXXX.'
            )

        return value

    def validate_email(self, value):
        value = value.lower().strip()

        if Profile.objects.filter(email=value).exclude(
            pk=self.instance.pk if self.instance else None
        ).exists():
            raise serializers.ValidationError(
                'This email is already registered.'
            )

        return value