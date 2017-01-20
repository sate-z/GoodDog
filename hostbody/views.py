# coding=utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from handle import upload_machine
import models
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def hostbody(request):
    return render(request, 'hostbody/hostbody.html')


def login_site(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {
                'login_err': 'Please recheck your username or password !'
            })
    return render(request, 'login.html')


@login_required
def logout_site(request):
    logout(request)
    return HttpResponseRedirect('/')

head_name = '阿里云 %s 机器列表'


@login_required
def ecs_list(request):
    host_list = models.HostInfo.objects.all()
    return render(request, 'hostbody/ecs_list.html', {'host_list': host_list, 'head_name': head_name % 'ECS'})


@login_required
def group_ecs_list(request):
    select_gid = request.GET.get('select_gid')
    print select_gid
    if select_gid:
        group = models.GroupInfo.objects.get(id=select_gid)
        print '====>', group
        host_list = group.host.select_related()
        print host_list
    else:
        host_list = []
    return render(request, 'hostbody/ecs_list.html', {'host_list': host_list, 'head_name': head_name % group})


@login_required
def bind_ecs_list(request):
    host_list = request.user.host.select_related()
    return render(request, 'hostbody/ecs_list.html', {'host_list': host_list, 'head_name': head_name % '独立主机'})


@login_required
def update_host(request):
    if upload_machine.save_host():
        return HttpResponseRedirect('/hostbody/ecs_list/')
    else:
        return render(request, 'hostbody/ecs_list.html', {'error_log': 'update failed'})


