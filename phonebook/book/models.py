from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=100)
    lastname = models.CharField(verbose_name="Lastname", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100, null = True)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    mobile_phone = models.CharField(verbose_name="Mobile phone", max_length=100)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Group(models.Model):
    name = models.CharField(max_length=128)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(Contact, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Contact, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
