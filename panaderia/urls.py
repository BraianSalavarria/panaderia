"""
URL configuration for panaderia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from Apps import empleados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/',include('Apps.ventas.urls',namespace='ventas')),
    path('empleados/',include('Apps.empleados.urls',namespace='empleados')),
    path('inventario/',include('Apps.inventario.urls',namespace='inventario')),
    path('',TemplateView.as_view(template_name='base/base.html'),name='home'),
    path('',include('Apps.usuario.urls',namespace='usuario')),
    
]
