"""ccalsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include, patterns

from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static

urlpatterns = [
    # ADMINISTRADOR DE DJANGO

    url(
        r'^admin/',
        admin.site.urls
    ),

    # FIN DEL ADMINISTRADOR DE DJANGO

    # INDEX : obvio esto es la pagina de inicio de todo tu sistema donde mostraras info irrelevante
    # como lo son: quienes somos, vision, mision etc... informacion estatica

    url(
        r'^$',
        'app.HOMEPAGE.views.index',
        name="index"
    ),

    # FIN DE INDEX

    # SISTEMA LOGIN

    #_login
    url(
        r'^login/$',
        login,
        {'template_name': 'ACCOUNTS/login.html'},
        name="login"
    ),

    #_signup + exito del usuario creado
    url(
        r'^crear_usuario/$',
        'app.ACCOUNTS.views.Registro_User',
        name="crear_usuario"
    ), url (
            r'^registro_exitoso/$',
            'app.ACCOUNTS.views.Registro_User_Success',
            name="registro_exitoso"
    ),

    #_logout
    url(
        r'^logout/$',
        logout,
        {'template_name': 'ACCOUNTS/logout.html'},
        name="logout"
    ),

    # FIN DE SISTEMA LOGIN

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
