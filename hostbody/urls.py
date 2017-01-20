from django.conf.urls import url
import views

app_name = 'hostbody'
urlpatterns = [
    url(r'^$', views.hostbody, name='hostbody'),
    url(r'^ecs_list/$', views.ecs_list, name='ecs_list'),
    url(r'^group_ecs_list/$', views.group_ecs_list, name='group_ecs_list'),
    url(r'^bind_ecs_list/$', views.bind_ecs_list, name='bind_ecs_list'),
    url(r'^update_host/$', views.update_host, name='update_host'),

]