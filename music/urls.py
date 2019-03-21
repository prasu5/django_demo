from django.conf.urls import url
from . import views
# from django.contrib import admin

app_name = 'music'

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
# ]{% url 'music:favorite' album.id %}
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
