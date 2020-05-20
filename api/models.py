from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Contact(models.Model):
    # account = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField("First name", max_length=30, blank=False, null=False)
    lastName = models.CharField("Last name", max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    # perception = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName, self.lastName


class Note(models.Model):
    body = models.TextField("Body", max_length=2000, blank=False, null=False)
    # account = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # contact = models.ForeignKey(Contact, default=1, on_delete=models.CASCADE, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Debt(models.Model):
    PROGRESS = (
        (0, 'In Progress'),
        (1, 'Paid')
    )
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    reason = models.CharField("Reason", max_length=255)
    progress = models.CharField("Progress", max_length=255, choices=PROGRESS)
    created = models.DateTimeField(auto_now_add=True)
    # contact = models.ForeignKey('Contact', default=1, on_delete=models.SET_DEFAULT, related_name='lender')

    '''
        The Debt object allows to record that you own to contacts, or what your contacts own you.
        A debt has to be linked to a contact
    '''

    def __str__(self):
        return self.contact

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
