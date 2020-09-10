from django.urls import path
from intlaqi import views

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('int_laqi', views.intl_aqi, name = 'intl_aqi'),
]