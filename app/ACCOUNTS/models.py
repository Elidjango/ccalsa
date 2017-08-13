#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from models import *

# Este es el modelo de crear nuevos usuarios, no modificar nada de aqui a menos que sepas los que
# haces.!!! xD

class login(models.Model):
    username = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        user ="%s" %(self.username) #si usa python3 el unicode es irrelevante. debe modificarlo a:
        return user                 #def __str__(self):
