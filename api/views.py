import os
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Contact, Note, Debt, Documents
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ContactSerializer, NoteSerializer, DebtSerializer, DocumentSerializer


class ContactList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class NoteList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DebtList(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DocumentUploadView(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    # API needs to know which headers to look for. Browsers transfer files as form-data
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        file = str(self.request.data.get('file'))
        # file_size = os.stat('static/{}'.format(file)).st_size
        # if file_size > 5242880:
        #     raise Response(status=status.HTTP_403_FORBIDDEN)
        serializer.save(
            # account=self.request.user,
            type=file[-3:],
            filesize=0,
            filename=file[:10]
        )
