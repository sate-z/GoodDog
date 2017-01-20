from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkcore import client
import json, pprint


class AliApi(object):
    def __init__(self, AccessKeyId, AccessKeySecret, Region):
        self.__AccessKeyId = AccessKeyId
        self.__AccessKeySecret = AccessKeySecret
        self.__Region = Region

    def ecs_api(self, PageNumber, PageSize):

        clt = client.AcsClient(self.__AccessKeyId, self.__AccessKeySecret, self.__Region)

        request = DescribeInstancesRequest.DescribeInstancesRequest()

        request.set_accept_format('json')
        request.set_PageNumber(PageNumber)
        request.set_PageSize(PageSize)
        result = clt.do_action(request)
        return json.loads(result)


if __name__ == '__main__':
    api = AliApi('LTAIibCw5AeNZtwS', '9MWiWxedTfmQbOhvDeFB3y4Q2OcUM2', 'cn-hangzhou')

    res = api.ecs_api(1, 1)
    print res

    res1 = api.ecs_api(1, 20)
    pprint.pprint(res1)