from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .serializers import ContactSerializer 
from rest_framework import generics


def home(request):
    return HttpResponse('Hello World')

class ContactListCreate(generics.ListCreateAPIView): 
    queryset = Contact.objects.all() 
    serializer_class = ContactSerializer
