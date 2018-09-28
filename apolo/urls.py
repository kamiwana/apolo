"""apolo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

admin.site.site_title = "MARGO OS Apolo Back-end System"
admin.site.site_header = "MARGO OS Apolo Back-end System"


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^file/', include('file.urls')),
    url(r'^docs/', include_docs_urls(title='Apolo API'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)