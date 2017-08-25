from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^$', views.sorry_list, name ='sorry_list'),
    url(r'^$', views.mainView, name ='sorry_list'),
    url(r'^sorry$', views.sorry_new, name='sorry_new'),
    url(r'^sorry/(?P<pk>\d+)/$', views.sorry_detail, name ='sorry_detail'),
    url(r'^ex$', views.sorry_filter_ex, name ='ex'),
    url(r'^family$', views.sorry_filter_fa, name ='fam'),
    url(r'^so$', views.sorry_filter_so, name ='so'),
    url(r'^friend$', views.sorry_filter_fr, name ='fr'),
    url(r'^enemy$', views.sorry_filter_en, name ='en'),
    url(r'^co$', views.sorry_filter_co, name ='co'),
    url(r'^str$', views.sorry_filter_st, name ='str'),

]
