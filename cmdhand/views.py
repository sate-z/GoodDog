# coding=utf-8
from django.shortcuts import render, HttpResponse
from hostbody import models
from django.contrib.auth.decorators import login_required
from cmdhandle import paramiko_handle
# Create your views here.


@login_required
def cmdhand(request):
    return render(request, 'cmdhand/cmdhand.html')


@login_required
def ecs_list(request):

    list_type = request.GET.get('type')

    if list_type == "grouphost":
        select_gid = request.GET.get('select_gid')
        if select_gid:
            group = models.GroupInfo.objects.get(id=select_gid)
            head_name = group
            host_list = group.host.select_related()
        else:
            host_list = []

    elif list_type == 'bindhost':
        print 'choose bindhost'
        head_name = '绑定主机'
        host_list = request.user.host.select_related()

    else:
        host_list = []

    return render(request, 'cmdhand/cmd_right.html', {'host_list': host_list, 'head_name': head_name})


@login_required
def cmd_handle(request):
    print request.POST
    login_user = request.POST.get('login_user')
    login_password = request.POST.get('login_pwd')
    host_list = request.POST.get('host_list')
    cmd = request.POST.get('cmd')
    host_list = host_list.split(',')[:-1]
    cmd_run = paramiko_handle.ParamikoHandle()
    print host_list
    for host in host_list:
        result = cmd_run.command_run(login_user, host, 22, cmd)
        print result

    return HttpResponse('get it')