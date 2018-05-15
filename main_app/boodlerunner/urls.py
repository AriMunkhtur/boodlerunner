from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^order/$', views.order, name='order'),
    url(r'^menu/$', views.menu, name='menu'),
	url(r'^updateRunner/$', views.updateRunner, name='updateRunner'),
    url(r'^updateReceiver/$', views.updateReceiver, name='updateReceiver'),
    url(r'^deliver/$', views.deliver, name='deliver'),
	url(r'^receipt/$', views.get_order, name='receipt'),

]