from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from .serializers import ContactSerializer, UserSerializer, UserSerializerWithToken


def home(request):
    return HttpResponse('Hello World')


# This view will be used anytime the user revisits the site, reloads the page, or does anything else that causes React to forget its state. React will check if the user has a token stored in the browser, and if a token is found, it’ll make a request to this view

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
