from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Contact, Journal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        # make password write only to hide it in GET requests. Will be required if request is POST
        extra_kwargs = {'password': {'write_only': True, 'required': True}, 'email': {'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # create user token on signup
        Token.objects.create(user=user)
        return user


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'first_name', 'last_name', 'nickname', 'gender', 'is_dead', 'email', 'phone',
            'description',
            'date_created')
        read_only_fields = ('date_created',)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ("id", "title", "body", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified",)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

# class DebtSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Debt
#         fields = ('id', 'account', 'amount', 'reason', 'progress', 'lender', 'date_created')
#         read_only_fields = ('date_created', 'date_modified')
#
#
# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = "__all__"
#         # read_only_fields = ('account', 'contact', 'date_created', 'date_modified')
#
