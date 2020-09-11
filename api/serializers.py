from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Contact, Journal, Debt, Note, Task, FoodPref


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


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'body', 'contact', 'date_created')
        read_only_fields = ('date_created', 'date_modified')
        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'contact', 'body', 'due_date', 'date_created')
        read_only_fields = ('date_created',)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class FoodPrefSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPref
        fields = ('id', 'body', 'contact')
        extra_kwargs = {
            'created_by': {'read_only': True}
        }


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'amount', 'reason', 'progress', 'contact', 'owes', 'date_created')
        read_only_fields = ('date_created', 'date_modified')


class ContactSerializer(serializers.ModelSerializer):
    debts = serializers.StringRelatedField(many=True)
    notes = serializers.StringRelatedField(many=True)
    tasks = serializers.StringRelatedField(many=True)
    foodprefs = serializers.StringRelatedField(many=False)

    class Meta:
        model = Contact
        fields = (
            'id', 'first_name', 'last_name', 'nickname', 'gender', 'is_dead', 'email', 'phone',
            'description', 'debts', 'notes', 'tasks', 'foodprefs', 'date_created')
        read_only_fields = ('date_created',)
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

        def create(self, validated_data):
            debts_data = validated_data.pop('debts')
            notes_data = validated_data.pop('notes')
            tasks_data = validated_data.pop('tasks')
            foodprefs_data = validated_data.pop('foodprefs')
            contact = Contact.objects.create(**validated_data)
            for debt_data in debts_data:
                Debt.objects.create(contact=contact, **debt_data)
            for note_data in notes_data:
                Note.objects.create(contact=contact, **note_data)
            for task_data in tasks_data:
                Task.objects.create(contact=contact, **task_data)
            for foodpref_data in foodprefs_data:
                    FoodPref.objects.create(contact=contact, **foodpref_data)
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
