from django.db import models
from django.contrib.auth.models import User


# from django.core.validators import MaxLengthValidator, MinLengthValidator
# from rest_framework import request, status
# from rest_framework.response import Response


class Contact(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField("First name", max_length=30, blank=False, null=False)
    last_name = models.CharField("Last name", max_length=30, blank=True, null=True)
    nickname = models.CharField("Nickname", max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=9, blank=False, null=False, choices=GENDER_CHOICES)
    is_dead = models.BooleanField(default=False)
    # perception = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName, self.lastName


class Note(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField("Body", max_length=2000, blank=False, null=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # def create(self, request, *args, **kwargs):
    #     user = User(created_by=self.request.user)
    #     serializer = self.serializer_class(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def __str__(self):
        return self.body


class Debt(models.Model):
    PROGRESS = (
        (0, 'In Progress'),
        (1, 'Paid')
    )
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    lender = models.ForeignKey(Contact, default=1, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    reason = models.CharField("Reason", max_length=255)
    progress = models.CharField("Progress", max_length=255, choices=PROGRESS)
    date_created = models.DateTimeField(auto_now_add=True)

    '''
        The Debt object allows to record that you own to contacts, or what your contacts own you.
        A debt has to be linked to a contact
    '''

    def __str__(self):
        return self.contact


# The Document object represents a document attached to a contact.
class Documents(models.Model):
    account = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, default=2, on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False, upload_to="static/")
    filename = models.CharField("filename", max_length=255, default='')
    filesize = models.IntegerField(default=0)
    type = models.CharField("type", max_length=30, default='')
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename

# class Country(models.Model):
#     name = models.CharField("Name", max_length=255, blank=False, null=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Address(models.Model):
#     name = models.CharField("Name", max_length=255, blank=False, null=True)
#     street = models.CharField("Street", max_length=255, blank=False, null=False)
#     city = models.CharField("City", max_length=255, blank=False, null=False)
#     province = models.CharField("Province", max_length=255, blank=False, null=False)
#     country = models.CharField("Country", max_length=255, blank=False, null=False)
#
#     # contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
