## docker 安装 ###

### centos 6.5 中docker的安装 ###

-  yum 源安装

```
$ yum install docker-io
```

- 启动

```
$ /etc/init.d/docker start
```

- 日志中报错

```
time="2016-01-19T14:21:25.993968299+08:00" level=warning msg="You are running linux kernel version 2.6.32-431.el6.x86_64, which might be unstable running docker. Please upgrade your kernel to 3.10.0." 
time="2016-01-19T14:21:25.997212022+08:00" level=info msg="Listening for HTTP on unix (/var/run/docker.sock)" 
/usr/bin/docker: relocation error: /usr/bin/docker: symbol dm_task_get_info_with_deferred_remove, version Base not defined in file libdevmapper.so.1.02 with link time reference
```
日志可以看出，一个warning和一个error。 warning中指出我的kernel版本可能运行docker不稳定，建议我升级到3.10版本。 error的报错可以通过升级device-mapper-libs解决。
```
yum upgrade device-mapper-libs
```
 
### centos 7 中docker的安装 ###
- yum 源安装

```
$ yum install docker
```