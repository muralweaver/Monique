from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField("First name", max_length=30, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=30, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)