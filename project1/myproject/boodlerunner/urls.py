from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]