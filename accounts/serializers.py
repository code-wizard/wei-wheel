from rest_framework import serializers
from accounts.models import LtUser, LtUserProfile
from django.db import transaction
from allauth.account.utils import send_email_confirmation


class LtRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, write_only=True)
    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=1000, write_only=True)

    def validate_email(self, email):
        if LtUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email

    def create(self, validated_data):
        first_name = validated_data.get("first_name","")
        last_name = validated_data.get("last_name","")

        with transaction.atomic():
            user = LtUser.objects.create(
                username=validated_data.get("email"),
                email=validated_data.get("email")
            )
            user.set_password(validated_data.get("password"))
            user.raw_password = validated_data.get("password")

            user.save()
            # send_email_confirmation(self.context.get("request"), user, True),

            profile = LtUserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
            profile.save()

            return user

    class Meta:
        model = LtUser
        fields = ("email","first_name","last_name","password")
        read_only_fields = ("paid_until",)
