"""hilltopTutorial URL Configuration

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
from django.urls import path, include

from django.views.generic.base import TemplateView

from . import views

from godjango.views import ProfileImageView, ProfileDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    
#    path(r'^$', TemplateView.as_view(template_name='index.html'),),

#    path(r'^calendar/', include('django_bootstrap_calendar.urls')),
    #path('hilltoptutorial', TemplateView.as_view(template_name='index.html'), ),
    path('index1', TemplateView.as_view(template_name='index1.html'), ),
    path('polls/', include('polls.urls')),
#    path(r'^', include('example.urls')) # tell django to read urls.py in example app
#    path('', include('example.urls')), # tell django to read urls.py in exampl$
    path('table2OneToMany/', include('table2OneToMany.urls')),
    path('oneTable/', include ('oneTable.urls')),
    path('godjango/', include ('godjango.urls')),
    path('simpleFileUpload/', include('simpleFileUpload.urls')),
#    path('uploadfile/', include('uploadfile.urls')),
#    path(r'^$, ProfileImageIndexView.as_view(), name='home'),
#    path(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
#    path(r'^uploaded/{?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile_image'),
] ## + sttatic(setings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
