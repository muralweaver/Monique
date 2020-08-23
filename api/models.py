from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField("First name", max_length=30, blank=False, null=False)
    last_name = models.CharField("Last name", max_length=30, blank=True, null=True)
    nickname = models.CharField("Nickname", max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=9, blank=False, null=False, choices=GENDER_CHOICES)
    is_dead = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name, self.last_name


class Journal(models.Model):
    title = models.CharField("Title", max_length=255, blank=False, null=False)
    body = models.TextField("Body", max_length=10000, blank=False, null=False)
    created_by = models.CharField(max_length=255)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Debt(models.Model):
    PROGRESS = (
        (0, 'In Progress'),
        (1, 'Paid')
    )
    lender = models.ForeignKey(Contact, default=1, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    reason = models.CharField("Reason", max_length=255)
    progress = models.CharField("Progress", max_length=255, choices=PROGRESS)
    created_by = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    '''
        The Debt object allows to record that you own to contacts, or what your contacts own you.
        A debt has to be linked to a contact
    '''

    def __str__(self):
        return self.contact


# The Document object represents a document attached to a contact.
# class Documents(models.Model):
#     contact = models.ForeignKey(Contact, default=2, on_delete=models.CASCADE)
#     file = models.FileField(blank=False, null=False, upload_to="static/")
#     filename = models.CharField("filename", max_length=255, default='')
#     filesize = models.IntegerField(default=0)
#     type = models.CharField("type", max_length=30, default='')
#     created_by = models.CharField(max_length=255)
#     date_modified = models.DateTimeField(auto_now=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.original_filename