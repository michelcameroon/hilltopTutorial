from django.urls import path

from . import views


from .views import ProfileImageView, ProfileDetailView

urlpatterns = [

    path(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    path(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image')

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



