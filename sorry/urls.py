from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.sorry_list, name ='sorry_list'),
    url(r'^sorry$', views.sorry_new, name='sorry_new'),
    url(r'^sorry/(?P<pk>\d+)/$', views.sorry_detail, name ='sorry_detail'),
]
