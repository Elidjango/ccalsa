#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, redirect, render_to_response, get_object_or_404

from django.template import Context
from django.template.context import RequestContext
from django.template.loader import get_template

from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import *
from .forms import *
# Create your views here.

# CREAR LOS NUEVOS USUARIOS
def Registro_User(request):
    if request.method == 'POST':  # Si el formulario ha sido enviado...
        form = RegistroForm(request.POST)  # Un formulario vinculado a los datos POST
        if form.is_valid():  # Todas las reglas de validación pasan

            # Procesar los datos en form.cleaned_data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

			# En este punto, el usuario es un objeto de usuario que ya se ha guardado
            # A la base de datos. Puede seguir cambiando sus atributos
            # Si desea cambiar otros campos.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name


			# Guardar nuevos atributos de usuario
            user.save()
            return HttpResponseRedirect('/registro_exitoso/')
            #tambien se puede usar
            #return HttpResponseRedirect(reverse('main.html'))  # Redirect after POST
    else:
        form = RegistroForm()

    data = {
        'form': form,
    }
    return render_to_response('ACCOUNTS/signup.html', data, context_instance=RequestContext(request))

# ESTO SALE SI EL USUARIO ES CREADO CON EXITO
def Registro_User_Success(request):
    return render_to_response('ACCOUNTS/success.html')
