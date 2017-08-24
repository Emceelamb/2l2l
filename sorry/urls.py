from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.sorry_list, name ='sorry_list'),
]
