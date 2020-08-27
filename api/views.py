# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
from django.http import Http404
from rest_framework.response import Response

from .models import Contact, Journal, Debt, Note, Task
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (ContactSerializer, UserSerializer, JournalSerializer, DebtSerializer, NoteSerializer,
                          TaskSerializer)
from django.contrib.auth.models import User


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


# https://github.com/encode/django-rest-framework/issues/2414
# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data["token"])
#         return Response({"token": token.key, "id": token.user_id})


class ContactList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        username = self.request.user.username
        serializer.save(created_by=username)

    def get_queryset(self):
        """
        This view should return a list of all Contacts
        for the currently authenticated user.
        """
        username = self.request.user.username
        return Contact.objects.filter(created_by=username)


class JournalList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        username = self.request.user.username
        serializer.save(created_by=username)

    def get_queryset(self):
        """
        This view should return a list of all Journal entries
        for the currently authenticated user.
        """
        username = self.request.user.username
        return Journal.objects.filter(created_by=username)


class NoteList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        username = self.request.user.username
        serializer.save(created_by=username)

    def get_queryset(self):
        username = self.request.user.username
        return Debt.objects.filter(created_by=username)


class TaskList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        username = self.request.user.username
        serializer.save(created_by=username)

    def get_queryset(self):
        username = self.request.user.username
        return Task.objects.filter(created_by=username)


class DebtList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        username = self.request.user.username
        serializer.save(created_by=username)

    def get_queryset(self):
        username = self.request.user.username
        return Debt.objects.filter(created_by=username)

# class DocumentUploadView(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
#     queryset = Documents.objects.all()
#     serializer_class = DocumentSerializer
#     # API needs to know which headers to look for. Browsers transfer files as form-data
#     parser_classes = (MultiPartParser, FormParser,)
#
#     def perform_create(self, serializer):
#         file = str(self.request.data.get("file"))
#         # file_size = os.stat('static/{}'.format(file)).st_size
#         # if file_size > 5242880:
#         #     raise Response(status=status.HTTP_403_FORBIDDEN)
#         serializer.save(
#             # account=self.request.user,
#             type=file[-3:],
#             filesize=0,
#             filename=file[:10]
#         )
