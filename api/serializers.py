from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'firstName', 'lastName', 'email', 'phone', 'description')
        
# We're subclassing ModelSerializer. A ModelSerializer in Django REST is like a ModelForm. It is suitable whenever you want to closely map a Model to a Serializer.