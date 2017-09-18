# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User
from .form import UserForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","first_name","last_name","telephone"]
    form = UserForm
    #class Meta:
        #model=User

admin.site.register(User,UserAdmin)