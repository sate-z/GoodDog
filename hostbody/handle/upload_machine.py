# coding=utf-8
from hostbody import models
import aliapi
from GoodDog import settings


def save_db(MachineInfo, region):
    print MachineInfo['InnerIpAddress']['IpAddress'][0]
    try:
        host = models.HostInfo(
            instance_id=MachineInfo['InstanceId'],
            custom_name=MachineInfo['InstanceName'],
            region=region,
            region_part=MachineInfo['ZoneId'],
            ip_public=MachineInfo['PublicIpAddress']['IpAddress'][0],
            ip_private=MachineInfo['InnerIpAddress']['IpAddress'][0],
            cpu_num=MachineInfo['Cpu'],
            memory=MachineInfo['Memory'],
            pay_type=MachineInfo['InstanceChargeType'],
            net_type=MachineInfo['InstanceNetworkType'],
            bandwidth=MachineInfo['InternetMaxBandwidthOut'],
            creation_time=MachineInfo['CreationTime'],
            expired_time=MachineInfo['ExpiredTime'],
        )
        host.save()
    except Exception, e:
        print 'some wrong', e

# def save_db1(MachineInfo, region):
#     host = {
#         'instance_id': MachineInfo['InstanceId'],
#         'custom_name': MachineInfo['InstanceName'],
#         'region_part': MachineInfo['ZoneId'],
#         'ip_public': MachineInfo['PublicIpAddress']['IpAddress'][0],
#         'ip_private': MachineInfo['InnerIpAddress']['IpAddress'][0],
#         'cpu_num': MachineInfo['Cpu'],
#         'memory': MachineInfo['Memory'],
#         'pay_type': MachineInfo['InstanceChargeType'],
#         'net_type': MachineInfo['InstanceNetworkType'],
#         'bandwidth': MachineInfo['InternetMaxBandwidthOut'],
#         'creation_time': MachineInfo['CreationTime'],
#         'expired_time': MachineInfo['ExpiredTime'],
#     }
#     print host


def save_host():
    api = aliapi.AliApi(settings.AccessKeyId, settings.AccessKeySecret, settings.Region)

    first_res = api.ecs_api(1, 1)
    TotalCount = first_res['TotalCount']
    TotalPageNum = int(TotalCount)/int(settings.PageSize) + 1

    try:
        for n in range(TotalPageNum):
            n += 1
            result = api.ecs_api(n, settings.PageSize)
            result_list = result['Instances']['Instance']
            print '执行save', n
            for i in result_list:
                save_db(i, settings.Region)
        return True
    except Exception, e:
        print e, '数据库错误'


