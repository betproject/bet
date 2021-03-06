from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries import CountryField

class Userbet(models.Model):
        user                    = models.OneToOneField(User)
        firstname               = models.CharField(max_length=100)
        name                    = models.CharField(max_length=100)
        birthday                = models.DateField()
        address			= models.CharField(max_length=200)
        postcode		= models.CharField(max_length=20)
        city			= models.CharField(max_length=50)
        country			= CountryField()
        status			= models.IntegerField(null=True)
        idcard			= models.IntegerField(null=True)

        def __unicode__(self):
                return self.name

