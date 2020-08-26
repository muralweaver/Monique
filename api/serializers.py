from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Contact, Journal, Debt


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


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'amount', 'reason', 'progress', 'contact', 'owes', 'date_created')
        read_only_fields = ('date_created', 'date_modified')


class ContactSerializer(serializers.ModelSerializer):
    debts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Contact
        fields = (
            'id', 'first_name', 'last_name', 'nickname', 'gender', 'is_dead', 'email', 'phone',
            'description', 'debts', 'date_created')
        read_only_fields = ('date_created',)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

        def create(self, validated_data):
            debts_data = validated_data.pop('debts')
            contact = Contact.objects.create(**validated_data)
            for debt_data in debts_data:
                Debt.objects.create(contact=contact, **debt_data)
            return contact


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ("id", "title", "body", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified",)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

#
# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = "__all__"
#         # read_only_fields = ('account', 'contact', 'date_created', 'date_modified')
#
