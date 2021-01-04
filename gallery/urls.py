from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_main'),
    path('view', views.view, name='view_main'),
]