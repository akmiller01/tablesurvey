from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name='core.views.index'),
    url(r'^edit/(?P<slug>[\w\-]+)/$', views.edit, name='core.views.edit'),
    url(r'^edit/(?P<slug>[\w\-]+)/(?P<year>\d{1,4})/$', views.edit, name='core.views.edit'),
    url(r'^accounts/login/$', views.login_user, name='core.views.login_user'),
    # url(r'^csv/(?P<slug>[\w\-]+)/$', views.csv,name="core.views.csv"),
    # url(r'^csv_all/$', views.csv_all,name="core.views.csv_all"),
    # url(r'^adminedit/(?P<slug>[\w\-]+)/(?P<year>\d{1,4})/$', views.adminEdit, name='core.views.adminEdit'),

]
