from django.urls import path

from .views import OneTableListView

urlpatterns = [
#    path('', views.index, name='index'),
    path('list', OneTableListView.as_view()), 
]

