from .views import ProfileImageIndexView

from .views import ProfileImageView, ProfileDetailView

urlpatterns = [

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
