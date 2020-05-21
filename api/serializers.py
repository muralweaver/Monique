from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Contact, Debt, Documents
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'account', 'firstName', 'lastName', 'email', 'phone', 'description', 'date_created')
        read_only_fields = ('date_created',)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'account', 'body', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'account', 'amount', 'reason', 'progress', 'lender', 'date_created')
        read_only_fields = ('date_created', 'date_modified')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"
        # read_only_fields = ('account', 'contact', 'date_created', 'date_modified')
