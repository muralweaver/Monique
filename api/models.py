from django.db import models


# Create your models here.


class Contact(models.Model):
    firstName = models.CharField("First name", max_length=30, blank=True, null=True)
    lastName = models.CharField("Last name", max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.firstName, self.lastName


class Country(models.Model):
    id = models.CharField("Id", max_length=255, blank=False, null=False, primary_key=True)
    name = models.CharField("Name", max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField("Name", max_length=255, blank=False, null=True)
    street = models.CharField("Street", max_length=255, blank=False, null=False)
    city = models.CharField("City", max_length=255, blank=False, null=False)
    province = models.CharField("Province", max_length=255, blank=False, null=False)
    country = models.CharField("Country", max_length=255, blank=False, null=False)

    # contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Note(models.Model):
    body = models.TextField("Body", max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.body
