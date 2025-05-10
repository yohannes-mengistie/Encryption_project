"""
URL configuration for encryptionProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path
from encryption.views import encrypt_message, decrypt_message
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os
from django.http import HttpResponse


def serve_react_index(request):
    index_path = os.path.join(settings.STATICFILES_DIRS[0], 'index.html')
    with open(index_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/html')
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('encrypt/',encrypt_message,name='encrypt'),
    path('decrypt/',decrypt_message,name='decrypt'),
    re_path(r'^.*$', serve_react_index, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])