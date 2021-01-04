from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_main'),
    url(r'^(?P<last_item>\d+)$', views.index, name='index_main'),
    path('view/<folder_name>', views.view, name='view_main'),
]