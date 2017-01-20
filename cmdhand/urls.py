from django.conf.urls import url
import views

app_name = 'cmdhand'
urlpatterns = [
    url(r'^$', views.cmdhand, name='cmdhand'),
    url(r'^ecs_list/$', views.ecs_list, name='ecs_list'),
    url(r'^cmd_handle/$', views.cmd_handle, name='cmd_handle'),
]