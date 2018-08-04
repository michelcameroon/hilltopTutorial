from django.urls import path

from .views import ProfileImageView

urlpatterns = [
#    path('', views.index, name='index'),
#    path('ProfileImageView', ProfileImageView.as_view()), 
    path('profile_image_form', ProfileImageView.as_view()),
]

