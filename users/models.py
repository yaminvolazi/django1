# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100,blank=False,null=True)
    last_name = models.CharField(max_length=100,blank=False,null=True)
    telephone = models.CharField(max_length=20,blank=False,null=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('update_user', kwargs={'pk': self.pk})