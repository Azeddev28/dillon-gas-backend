from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class ResetPasswordSerializedr(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()
    verification_code = serializers.CharField()

    def validate(self, attrs):
        result = super().validate(attrs)
        if attrs.get('new_password') != attrs.get('confirm_password'):
            raise serializers.ValidationError(
                {'password': "Passwords must Match"})

        email = attrs.get('email')
        user = None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            msg = 'User does not exist'
            raise serializers.ValidationError(msg)

        verification_code = attrs.get('verification_code')
        if self.context['request'].session.get('verification_code') != verification_code:
            raise serializers.ValidationError(
                {'verification_code': 'Invalid Verification Code!'}
            )
        result['user'] = user
        return result
