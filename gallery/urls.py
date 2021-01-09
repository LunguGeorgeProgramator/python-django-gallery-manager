from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_main'),
    url(r'^(?P<last_item>\d+)$', views.index, name='index_main'),
    path('search', views.search, name='search_main'),
    url(r'^search/(?P<search>.+)$', views.search, name='search_main'),
    path('view/<folder_name>', views.view, name='view_main'),
    url(r'^view/(?P<folder_name>.+)/(?P<last_item>\d+)$', views.view, name='view_main'),
    path('rename', views.renameDir, name='rename_main'),
    path('delete', views.removeDir, name='delete_main'),
]