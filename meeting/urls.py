from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'meeting'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

admin.site.site_header = "Meetings App"
admin.site.site_title = "Meetings App"
admin.site.index_title = "Meetings App"