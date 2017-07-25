# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class UserModel(models.Model):
    username = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
