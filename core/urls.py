from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name='core.views.index'),
    url(r'^edit/(?P<slug>[\w\-]+)/$', views.edit, name='core.views.edit'),
    url(r'^edit/(?P<slug>[\w\-]+)/(?P<year>\d{1,4})/$', views.edit, name='core.views.edit'),
    url(r'^accounts/login/$', views.login_user, name='core.views.login_user'),
    url(r'^export/(?P<slug>[\w\-]+)/$', views.export, name="core.views.export"),
    url(r'^export/$', views.export, name="core.views.export"),
]
